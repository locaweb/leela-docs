============================
 Architecture in a nutshell
============================

Following a high level description of its main components:

.. image:: https://docs.google.com/drawings/pub?id=10lnt1ADTlG0WNhYBEDBBKTnCwn3n7fVBzpNgyhN8XNA&w=960&h=720
   :height: 720px
   :width: 960px
   :alt: architecture
   :align: center

LeCore
======

It is the engine that supports the entire stack of leela. By design it
has a very small set of primitives. Its sole purpose is to provide the
foundation necessary to enable frontends (e.g. leela-server) to create
a richer set of features.

This is the component responsible for managing the storage backends [=
*store*, *load* & *delete*] and provides the primitives to monitor
real time events [= *watch*].

It also allows you to transform the data through a very simple
map-reduce API.

Currently it uses cassandra, for now its sole storage backend, to
store data.

Frontend
========

It provides an interface to manage the data [through the core] using a
rich set of protocols. For instance, the HTTP interface is for
retrieving stored data using JSON format, whereas the XMPP interface
is designed to monitoring real time events.

Redis is used by the frontend to various, low volume, administrative
tasks, like propagating xmpp channels through the possibly many
instances of leela-server frontends.
