================
 HTTP Interface
================

This exposes data via a *REST* interface. The following should apply
to all resources:

* All resources support the *JSON-P* protocol by appending the
  ``callback`` parameter to the URL::

  /v1/foobar?callback=my_handler

* Currently only JSON format is supported;

* Brackets means that component is optional. For instance
  ``/v1/[data/]foobar`` represents two distinct resources:

  a. ``/v1/foobar``

  b. ``/v1/data/foobar``

* You may add ``debug=true`` to enable debug information, as follows
  (defaults to ``false``)::

  /v1/foobar?debug=true

Resources
=========

/v1/[data/]:year/:month/:key
----------------------------

Retrieves data from the given month.

:key: the event to load [e.g. localhost.cpu.idle];
:year: the year [4 digits];
:month: the month [numeric, starts with 1];

/v1/[data/]:year/:month/:day/:key
---------------------------------

Retrieves data from the given day.

:key: the event to load [e.g. localhost.cpu.idle];
:year: the year [4 digits];
:month: the month [numeric, starts with 1];
:day: the day of month [numeric, starts with 1];

/v1/[data/]past24/:key
----------------------

Retrieves data from the past 24 hours.

:key: the event to load [e.g. localhost.cpu.idle];

/v1/[data/]pastweek/:key
------------------------

Retrieves data from the past week (7 days).

:key: the event to load [e.g. localhost.cpu.idle];

/v1/[data/]range/:key?start=TIMESPEC&finish=TIMESPEC
----------------------------------------------------

Retrieves data within a given time range.

:key: The event to load [e.g. localhost.cpu.cpu.idle];
:start: The start date, UTC. Make sure ``start <= finish``;
:finish: The finish date, UTC. Make sure the ``finish >= start``;
:TIMESPEC: ``:YEAR:MONTH:DAYT:HOUR:MINUTE`` [e.g. 20120101T2040].

PUT /v1/data/:key
-----------------

Inserts a new data value under this key. The body of the request must
be a valid json, and the json must have at least the following keys:

:name: The name to store this object. This must match with the name
       given in the URL;
:timestamp: Unix timestamp (number of seconds since epoch);
:value: The value to store under this key/timestamp;

Example::

  $ curl -X PUT -d '{"name": "foobar", "timestamp": 1352483918, "value": :VALUE}'
  { "status": 201,
    "results": {"name": "foobar", "timestamp": 1352483918, "value": :VALUE}
  }

Response Codes
==============

:2xx: Ok;

:200: Success;

:201: Created;

:4xx: Client error;

:404: The requested data could not be found (invalid range, missing
      event etc.);

:400: You did something wrong;

:5xx: Server error;

:500: Internal server error;

:503: Maintanance;

Payload failure case
--------------------

::

  {"status": int, "reason": string}

:status: the http response code (e.g. 200, 400);
:reason: a very short description of what went wrong;

Example:

::

  {"status": 404, "reason": "no event found"}


Payload success case
--------------------

::

  { "results": { KEY: { "series": TIMESERIES
                      }
               },
    "status": 200
  }

:KEY: the event requested;
:TIMESERIES: A list with a 2-tuple ``[timestamp, value]``;

Example:

::

  { "results": { "localhost.cpu.idle": { series: [ [0,  0],
                                                   [60, 12.5]
                                                 ]
                                       }
               },
    "status": 200
  }
