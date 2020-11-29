
{}:

let pkgs = import /Users/nkpart/p/nixpkgs {};
    qpageview = pkgs.python38.pkgs.buildPythonPackage rec {
      pname = "qpageview";
      version = "1.0";
      # TODO replace with https://github.com/frescobaldi/qpageview
      src = ./qpageview;
      doCheck = false;

      propagatedBuildInputs = with pkgs.python38Packages; [ pyqt5 ];

    };

    pyEnv2 = pkgs.python38.buildEnv.override {
        extraLibs = with pkgs.python38.pkgs; [
        pyqt5 
        poppler-qt5
        qpageview
        python-ly
        ];

        ignoreCollisions = true;
    };

    qtbase = pkgs.qt5.qtbase;
    qtv = qtbase.version;
in
  pkgs.mkShell {
    # this will make all the build inputs from hello and gnutar
    # available to the shell environment
    # inputsFrom = with pkgs; [ mypi ];

    QT_QPA_PLATFORM_PLUGIN_PATH="${qtbase}/lib/qt-${qtv}/plugins";
    # QT_MAC_WANTS_LAYER = 1;

    buildInputs = [ 
        pyEnv2
        pkgs.qt5.qtbase
     ];
  }
