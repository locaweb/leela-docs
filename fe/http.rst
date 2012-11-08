================
 HTTP Interface
================

This exposes data via a *REST* interface. The following should apply
to all resources:

* All resources support the *JSON-P* protocol by appending the
  ``callback`` parameter to the URL::

  /v1/foobar?callback=my_handler

* Currently only JSON format is supported;

* Brackets in URLs means optional arguments. For instance
  ``/v1/[data/]foobar`` represents two distinct resources:

  a. /v1/foobar
  b. /v1/data/foobar

* You may add ``debug=true`` to enable debug information, as follows
  (defaults to ``false``):

  /v1/foobar?debug=true

Resources
=========

/v1/[data/]:year/:month/:key
---------------------

Retrieves data from the given month.

:key: the event to load [e.g. localhost.cpu.idle];
:year: the year [4 digits];
:month: the month [numeric, starts with 1];

/v1/[data/]:year/:month/:day/:key
--------------------------

Retrieves data from the given day.

:key: the event to load [e.g. localhost.cpu.idle];
:year: the year [4 digits];
:month: the month [numeric, starts with 1];
:day: the day of month [numeric, starts with 1];

/v1/[data/]past24/:key
---------------

Retrieves data from the past 24 hours.

:key: the event to load [e.g. localhost.cpu.idle];

/v1/[data/]pastweek/:key
-----------------

Retrieves data from the past week (7 days).

:key: the event to load [e.g. localhost.cpu.idle];

/v1/[data/]range/:key?start=TIMESPEC&finish=TIMESPEC

Retrieves data within a given time range.

:key: The event to load [e.g. localhost.cpu.cpu.idle];
:start: The start date. Make sure ``start <= finish``;
:finish: The finish date. Make sure the ``finish >= start``;
:TIMESPEC: %Y%m%dT%H%M [e.g. 20120101T2040];

Response Codes
==============

:200: Success;

:404: the requested data could not be found (invalid range, missing
      event etc.);

:500: internal server error;

:400: you did something wrong;

Payload: failure case
---------------------

::

  {"status": int, "reason": string}

:status: the http response code (e.g. 200, 400);
:reason: a very short description of what went wrong;

Example:

::

  {"status": 404, "reason": "no event found"}


payload: success case
---------------------

::

  { "results": { KEY: { "series": TIMESERIES
                      }
               }
  }

:KEY: the event requested;
:TIMESERIES: A list with a 2-tuple ``[timestamp, value]``;

Example:

::

  { "results": { "localhost.cpu.idle": { series: [ [0,  0],
                                                   [60, 12.5]
                                                 ]
                                       }
               }
  }
