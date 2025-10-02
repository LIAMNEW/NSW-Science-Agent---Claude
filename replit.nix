{ pkgs }: {
  deps = [
    pkgs.google-cloud-sdk
    pkgs.replitPackages.prybar-python310
    pkgs.replitPackages.stderred
  ];
}