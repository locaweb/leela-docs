===============
 UDP Interface
===============

The protocol is fairly simple:

::

  <name>: <value> [timestamp]\n

:name: Any unicode string (ascii encoded), up to 255 characters;

:value: Any double value (e.g.: 0.0, nan, 3.2e12);

:timestamp: [optional] the unix timestamp you want to store this
  event. If you don't provide this value the server will use the
  current timestamp;

There is no *ack* [=confirmation the event was received], nor
authentication, nor checksum [application level] whatsoever. If you
need such a feature, use a different protocol [e.g. TCP].

Example
=======

Assuming you have ``netcat``, and the server up and running, the following
shell commands should work:

::

  $ echo "example.e0: 0.75 1350332001" | nc -u localhost 6968
  $ echo "example.e0: 0.76"            | nc -u localhost 6968
