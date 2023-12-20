{pkgs}: {
  deps = [
    pkgs.gti
    pkgs.glibcLocales
    pkgs.glibc
  ];
  env = {
    PYTHON_LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
      pkgs.glibcLocales
    ];
  };
}
