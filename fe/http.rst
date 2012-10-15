===============
 HTTP Protocol
===============

This exposes data via a *REST* interface. The following should apply
to all resources:

* All resources support the *JSON-P* protocol by appending the
  ``callback`` parameter to the URL;

* Currently only JSON format is supported;

Resources
=========

/v1/:year/:month/:key
---------------------

Retrieves data from the given month.

:key: the event to load [e.g. localhost.cpu.idle];
:year: the year [4 digits];
:month: the month [numeric, starts with 1];

/v1/:year/:month/:day/:key
--------------------------

Retrieves data from the given day.

:key: the event to load [e.g. localhost.cpu.idle];
:year: the year [4 digits];
:month: the month [numeric, starts with 1];
:day: the day of month [numeric, starts with 1];

/v1/past24/:key
---------------

Retrieves data from the past 24 hours.

:key: the event to load [e.g. localhost.cpu.idle];

/v1/pastweek/:key
-----------------

Retrieves data from the past week (7 days).

:key: the event to load [e.g. localhost.cpu.idle];

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

  {"code": int, "message": string}

:code: the http response code (e.g. 200, 400);
:message: a very short description of what went wrong;

Example:

::

  {"code": 404, "message": "no event found"}


payload: success case
---------------------

::

  { "debug": { "request_uri": string
             , "request_time": float
             }
  , "results": { KEY: { "series": TIMESERIES
                      }
               }
  }

:KEY: the event requested;
:TIMESERIES: A list with a 2-tuple ``[timestamp, value]``;

Example:

::

  { "debug": { "request_uri": "/v1/past24/localhost.cpu.idle"
             , "request_time": 0.002
             }
  , "results": { "localhost.cpu.idle": { series: [ [0,  0],
                                                   [60, 12.5]
                                                 ]
                                       }
               }
  }
