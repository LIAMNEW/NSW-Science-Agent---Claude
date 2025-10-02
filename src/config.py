import os

PROJECT_ID = os.getenv('GOOGLE_CLOUD_PROJECT', 'nsw-science-learning')
LOCATION = os.getenv('GOOGLE_CLOUD_LOCATION', 'us-central1')
MODEL_NAME = 'gemini-2.0-flash-exp'

NESA_CURRICULUM_UNITS = [
    {
        'unit': 'Observing the universe',
        'code': 'SC4-OUT-01',
        'topics': ['astronomy', 'space science', 'observations'],
        'working_scientifically': ['SC4-WS-01', 'SC4-WS-04', 'SC4-WS-06', 'SC4-WS-08']
    },
    {
        'unit': 'Forces',
        'code': 'SC4-FOR-01',
        'topics': ['forces', 'motion', 'energy', 'friction'],
        'working_scientifically': ['SC4-WS-01', 'SC4-WS-02', 'SC4-WS-06']
    },
    {
        'unit': 'Cells and classification',
        'code': 'SC4-CEL-01',
        'topics': ['cells', 'microscope', 'classification', 'organisms'],
        'working_scientifically': ['SC4-WS-01', 'SC4-WS-04', 'SC4-WS-08']
    },
    {
        'unit': 'Solutions and mixtures',
        'code': 'SC4-SOL-01',
        'topics': ['mixtures', 'solutions', 'separation', 'matter'],
        'working_scientifically': ['SC4-WS-02', 'SC4-WS-06', 'SC4-WS-08']
    },
    {
        'unit': 'Rock Cycle',
        'code': 'SC4-GEA-01',
        'topics': ['rocks', 'minerals', 'rock cycle', 'geology'],
        'working_scientifically': ['SC4-WS-01', 'SC4-WS-04', 'SC4-WS-06']
    },
    {
        'unit': 'Energy',
        'code': 'SC4-ENE-01',
        'topics': ['energy types', 'energy transfer', 'conservation of energy'],
        'working_scientifically': ['SC4-WS-02', 'SC4-WS-06', 'SC4-WS-08']
    }
]

WORKING_SCIENTIFICALLY_SKILLS = {
    'SC4-WS-01': 'Using scientific tools and instruments safely for observations',
    'SC4-WS-02': 'Planning and conducting investigations',
    'SC4-WS-04': 'Processing data and identifying patterns',
    'SC4-WS-06': 'Using data to draw conclusions',
    'SC4-WS-08': 'Communicating scientific ideas'
}
