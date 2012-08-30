==============
 UDP Protocol
==============

When using UDP, the protocol is fairly simple:

::

  <name>: <value> [timestamp] [tags]\n

:name: Any string, up to 255 characters;

:value: Any double value;

:timestamp: [optional] the unix timestamp you want to store this
  event. If you don't provide this value the server will use the
  current timestamp;

:tags: [optional] the current flags are currently defined:

       :T: mark the event as transient, i.e., data will not be
           persisted (useful for high-frequency data that you only
           want to monitor);

There is no *ack* [=confirmation the event was received]
whatsoever. There is no authentication nor authorization. Also
remember the transport protocol is *UDP*.

If you need such a features, use a different protocol.

Example
=======

Assuming you have ``netcat``, and the server up and running, the following
shell commands should work:

::

  $ echo "example.e0: 0.75" | nc -u localhost 6968
  $ echo "example.e1: 0.76" | nc -u localhost 6968
