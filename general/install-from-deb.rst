===============================
 Installing the Debian Package
===============================

Currently we don't provide any binary packages, so you must build it
on your own. Although the package is suitable for using with debian
stables [= squeeze at the time we wrote this] building it depends on
packages only found on experimental branch: ``ghc`` and
``cabal-install``.

If you can workaround these, building it should be fairly
straightforward: ::

  $ git clone git://github.com/locaweb/leela.git
  $ cd leela
  $ debuild

After that you can install it using ``dpkg``: ::

  $ sudo dpkg -i ../leela_<version>_<arch>.deb
  $ sudo apt-get -f install
