==========
 Protocol
==========

The protocol is fairly simple:
::

  <name>: <value> [timestamp]\n

:name: Any string, up to 255 characters;

:value: Any double value;

:timestamp: [optional] the unix timestamp you want to store this
  event. If you don't provide this value the server will use the
  current timestamp;

Example
=======

The following are examples of well-formed events:

::

  "leela.protocol: 0.75\n"

  "leela.protocol2: 0.78 3600\n"
