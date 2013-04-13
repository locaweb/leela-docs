==============================
 Installing the Linux Tarball
==============================

Requirements
============

* python2

* virtualenv

* ghc7

* cabal

On arch linux, the above can be fulfilled using pacman:

.. code-block:: sh

  $ pacman -S python2-virtualenv cabal-install

Now, download the latest release from github and build it:

.. code-block:: sh

  $ wget -Oleela-v2x.tar.gz https://github.com/locaweb/leela/archive/v2.x.tar.gz
  $ tar -xf leela-v2x.tar.gz
  $ cd leela-2.x
  $ make bootstrap
  $ make dist-build

And install it:

.. code-block:: sh

  $ root=/opt/leela
  $ make dist-install root=$root

You should check the configuration file [= `$root/etc/leela.conf`] and
make sure everything checks out. After that, start the service.

.. code-block:: sh

  $ $root/etc/init.d/leela start
