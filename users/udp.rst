===============
 UDP Interface
===============

This is a write-only interface. It uses UDP and the protocol is plain
text. The protocol is fairly simple:

::

  <type> <length>|<key> <value>[ timestamp];

:type: * gauge
       * derive
       * counter
       * absolute

:length: The size of the *key* string;

:key: Any string (ascii encoded), up to 255 characters;

:value: Any double value (e.g.: 0.0, nan, 3.2e12);

:timestamp: [optional] the unix timestamp you want to store this
            event. If you don't provide this value the server will use
            the current timestamp;

There is no *ack* [=confirmation the event was received], nor
authentication, nor checksum [application level] whatsoever. If you
need such a feature, use a different protocol [e.g. collectd].

N.B.: There is no trailing newline here. Adding a trailing newline is a parser error.

PING
====

The UDP protocol is also capable of receiving a PING message that can
use used to test connectivity. The syntax is as follows:
::

  ping\n

Examples
========

Assuming you have `netcat`, and the server up and running, the following
shell commands should work:

::

  # the ping message
  $ echo ping                                      | nc -u localhost 6968
  pong

  $ echo -n "gauge 10|example.e0 0.75 1350332001;" | nc -u localhost 6968
  $ echo -n "derive 10|example.e0 0.76;"           | nc -u localhost 6968

Legacy udp protocol
===================

This protocol is deprecated. It will be removed in future releases:
::

  <name>: <value>[ timestamp]\n
