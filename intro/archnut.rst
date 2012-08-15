============================
 Architecture in a nutshell
============================

Leela has four main components:

Core
====

It is the engine that supports the entire stack of leela. By design it
has a very small set of features. Its purpose is to provide the
primitives necessary to enable frontends (e.g. leela-server) to create
a richer set of features. You, as a client, only interact with the
core through one of its frontends.

This is the component responsible for managing the storage backend
(w.r.t. reads and writes) whenever that is and provides the primitives
to monitor and analyze the data.

Server
======

The frontend that exposes serveral interfaces (UDP, TCP, HTTP, XMPP)
to interact with the core.

In some sense you may think of it as a transport layer.

Client
======

A Python API that provides you the means to communicate with the
server.

Relay
=====

TODO:fixme
