====================
 Leela Architecture
====================

Leela is designed to run on Linux. Although I believe it should works
on other POSIX platforms, the only environment we have tested it is
Linux.

It makes heavy use of unix sockets (mostly datagrams) and is currently
written in python and haskell. The following diagram summarizes the
major components:

.. blockdiag::

  blockdiag {

    group {
      orientation = portrait
      color = "#ffffff";

      dmproc <-> leela_xmpp;
    }

    leela_udp, leela_collectd, leela_http -> timeline;

    timeline -> dmproc, leela_storage;

    dmproc -> leela_xmpp;

    leela_xmpp -> ejabberd, redis-server;

    leela_storage -> cassandra;

    leela_http    -> timeline;
  }

In the above diagram all components communicate using unix sockets,
but external systems [cassandra, redis-server and ejabberd] which use
TCP. This [the use of unix sockets] implies that everything must run
on the same machine, or that you will a machine with a reasonable
number of cores to sustain high loads.

Following we provide more details about each component and how they
interact with each other.

Leela UDP/Collectd
==================

They simply parse the packet and forward to the timeline using the
leela internal protocol.

Leela HTTP
==========

This exposes the rest API which allows you to retrieve historical
data. It reads data from cassandra directly but in the future all
reading and writing to the storage will be go through the
leela-storage service.

The HTTP provides a read/write interface. Writing are simply forward
to the timeline, as the previous components do.

Timeline
========

This is the only component that effectively knows about metrics. You
may think of it as a function that takes a *metric* and produces one
or more *events* [an event is just a gauge type].

The process exposes the following unix sockets:

.. blockdiag::

   blockdiag {

     databus   [shape = endpoint];
     multicast [shape = endpoint];

     databus -> timeline -> multicast;

   }

The databus socket is the one metrics should arrive. Each frontend
[udp, collectd, http] writes one or more metrics into it. Then, if any
given metric generates any event then the timeline writes them into
the connected peers. This is done using the *multicast* unix socket.

Interested processes should continuously register themselves using the
*multicast* socket in order to receive the events that the timeline
generates.

The reason this must be a continuous operation is that the timeline
purges dead nodes, i.e., nodes that are not sending register messages
in a timely manner.

DMPROC
======

.. blockdiag::

   blockdiag {
     databus [shape = endpoint];
     proc    [shape = endpoint];

     databus -> dmproc <-> proc;
   }

This is the engine that allows users to monitor metrics as soon as
they are received. Once started, it register itself in timeline in
order to receive events into the *databus* socket, and exposes its
service through the *proc* socket.

The proc socket is the only one that is stream oriented. The
protocol is fairly simple though. It prefixes all packets with its
size, using a unsigned short [2 bytes] big endian encoded.

::

  0                       2
  |           |           |
  ------------+-----------+
  |         size          |
  +-----------------------+
  |                       |
  |        payload        |
  |        (0-65k)        |
  |                       |
  +-----------------------+

Leela XMPP
==========

Exposes its services as an user of a XMPP service using a language
that resembles SQL. This module allows one to monitor metrics in real
time via XMPP.

.. blockdiag::

   blockdiag {
     proc [shape = endpoint];
     databus [shape = endpoint];

     timeline -> databus -> dmproc;
     leela_xmpp -> ejabberd, redis;
     leela_xmpp <-> proc <-> dmproc;
   }

The redis is used as a directory service. When a request is made by a
user an new entry is written into the redis. Periodically, leela
xmpp service reads from redis in order to know which users are
requesting information. When a new entry is found, it establishes a
connection with dmproc and any output is forwarded via XMPP to the
users requesting the information. Similarly, whenever an entry is
removed from redis the associated connection with dmproc is closed.

The load on a redis server is very low, but it is extremely important
to make sure it is always available. If the redis service become
unavailable, so does the leela-xmpp.
