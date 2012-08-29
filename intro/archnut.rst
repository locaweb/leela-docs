============================
 Architecture in a nutshell
============================

Leela in a nutshell is a toolbox that allows you to analyze and
monitor real time events.

The main abstraction is the event, which is a key-value pair that the
system stores and allows you to retrieve and monitor using a very rich
set of protocols.

Examples of usage including graphing the cpu usage from the past of a
set of machines, or monitoring memory consumption and triggering
alerts when it hits a given threshold.

.. image:: https://docs.google.com/drawings/pub?id=10lnt1ADTlG0WNhYBEDBBKTnCwn3n7fVBzpNgyhN8XNA&w=960&h=720
   :height: 720px
   :width: 960px
   :alt: architecture
   :align: center

LeCore
====

It is the engine that supports the entire stack of leela. By design it
has a very small set of primitives. Its purpose is to provide the
features necessary to enable frontends (e.g. leela-server) to create a
richer set of functionality.

This is the component responsible for managing the storage backends
[=store, load & delete] and provides the primitives to monitor
[=watch].

Also it allows you to transform the data through a very simple
map-reduce API.

Frontend
========

The main purpose is to enable clients to interact with the *lecore*
component. It exposes several protocols for that purpose, for
instance, the xmpp protocol is used to monitor real-time data.

As the core is minimalist, it adds important layers to the stack, for
instance authentication.

Cassandra
=========

The default storage backend, managed by the core.

Redis
=====

Used by the frontend to various, low volume, administrative tasks.
