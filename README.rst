=====
LEELA
=====

This project is the documentation for the first version of
[Leela project](https://github.com/locaweb/leela), and it is published on
[Read the Docs](http://leela.rtfd.org/).

Contributing
============

The following will install sphinx using virtualenv and start the
server:
::

  $ git submodule init
  $ git submodule update
  $ ./scripts/bootstrap.sh

The documentation should now be available here:
::

  $ open http://localhost:4080

This script auto detects file modifications and rebuild the
documentation.
