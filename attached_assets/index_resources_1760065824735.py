# index_resources.py
import os
import importlib.util
import sys
from google.cloud import aiplatform
from google.cloud import discoveryengine_v1beta as de
from google.protobuf import struct_pb2
from google.api_core.exceptions import AlreadyExists, NotFound

# --- Config ---
PROJECT_ID = "hale-mercury-471604-d0"
LOCATION = "global"
DATA_STORE_ID = "bucketeducationagent_store"
RESOURCE_CATALOG_FILE = "resource_catalog.py"
SYLLABUS_GCS_URI = "gs://bucketeducationagent/science-and-technology-k-6-syllabus-2017.pdf"


def load_resource_catalog(file_path: str):
    """Dynamically load resources list from resource_catalog.py"""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Resource catalog file not found at: {file_path}")
    spec = importlib.util.spec_from_file_location("resource_catalog", file_path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["resource_catalog"] = mod
    spec.loader.exec_module(mod)
    return getattr(mod, "resources", None)


def create_vertex_ai_search_index(project_id: str, location: str, data_store_id: str, resources_data: list, syllabus_gcs_uri: str):
    aiplatform.init(project=project_id, location=location)

    ds_client = de.DataStoreServiceClient()
    doc_client = de.DocumentServiceClient()

    loc_path = f"projects/{project_id}/locations/{location}"
    collection = "default_collection"
    data_store_parent = f"{loc_path}/collections/{collection}"

    # ---- Create or reuse DataStore ----
    print(f"Creating data store '{data_store_id}' in location '{location}'...")
    ds = de.DataStore(
        display_name=data_store_id,
        industry_vertical=de.IndustryVertical.GENERIC,
        solution_types=[de.SolutionType.SOLUTION_TYPE_SEARCH],
    )
    try:
        op = ds_client.create_data_store(
            request=de.CreateDataStoreRequest(
                parent=data_store_parent,
                data_store_id=data_store_id,
                data_store=ds,
            )
        )
        data_store = op.result()
        data_store_name = data_store.name
        print(f"Data store created: {data_store_name}")
    except AlreadyExists:
        data_store_name = f"{data_store_parent}/dataStores/{data_store_id}"
        print(f"Data store already exists, reusing: {data_store_name}")

    # ---- Upload documents ----
    branch = "default_branch"
    documents_parent = f"{data_store_name}/branches/{branch}"
    print(f"\nUploading {len(resources_data)} resources to '{documents_parent}'...")

    for r in resources_data:
        s = struct_pb2.Struct()
        s.update({
            "title": r.get("Resource.Title", ""),
            "resource_type": r.get("Resource.Type", ""),
            "curriculum_alignment": r.get("Curriculum.Alignment", {}),
            "learning_objective": r.get("Pedagogy.Learning_Objective", ""),
            "intended_agent": r.get("Pedagogy.Intended_Agent", ""),
            "difficulty_level": r.get("Metadata.Difficulty_Level", ""),
            "source": r.get("Metadata.Source", ""),
            "description": r.get("Metadata.Description", ""),
            "original_url": r.get("Resource.URL", ""),
        })

        doc = de.Document(
            id=r.get("ID"),
            struct_data=s,
            derived_struct_data={"content_uri": r.get("Resource.URL", "")},
        )

        if r.get("ID") == "nesa_syllabus_s4_v1":
            s.update({"gcs_path": syllabus_gcs_uri})
            doc.struct_data = s

        name = f"{documents_parent}/documents/{r.get('ID')}"
        try:
            _ = doc_client.get_document(name=name)
            print(f"  ↷ Skipped (exists): {name}")
            continue
        except NotFound:
            pass

        try:
            created = doc_client.create_document(
                request=de.CreateDocumentRequest(
                    parent=documents_parent,
                    document=doc,
                    document_id=r.get("ID"),
                )
            )
            print(f"  ✓ Indexed: {created.name}")
        except AlreadyExists:
            print(f"  ↷ Skipped (race): {name}")
        except Exception as e:
            print(f"  ✗ Error indexing '{r.get('ID')}': {e}")

    print("\nFinished uploading resources.")


if __name__ == "__main__":
    try:
        resources = load_resource_catalog(RESOURCE_CATALOG_FILE)
        if not resources:
            print("No resources loaded. Exiting.")
        else:
            print(f"Loaded {len(resources)} resources from '{RESOURCE_CATALOG_FILE}'.")
            create_vertex_ai_search_index(
                project_id=PROJECT_ID,
                location=LOCATION,
                data_store_id=DATA_STORE_ID,
                resources_data=resources,
                syllabus_gcs_uri=SYLLABUS_GCS_URI,
            )
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
