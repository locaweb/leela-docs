==========
 REST API
==========

This exposes datas via a *REST* interface. The following should apply
to all resources:

* All resources support the *JSON-P* protocol by appending the
  ``callback`` parameter to the URL: ::

  /v1/foobar?callback=my_handler

* You may add ``debug=true`` to enable debugging information. This can
  give you a hint of what went wrong: ::

  /v1/foobar?debug=true

Common Response Codes
=====================

:2xx: Ok;
:4xx: Client error;
:5xx: Server error;
:200: Success;
:201: Created;
:404: The requested data could not be found [invalid range, missing
      event etc.];
:400: You did something wrong;
:500: Internal server error;

Error Responses
===============

They will always come using the following format:

::

  {"status": int, "reason": string}

:status: the http response code [e.g. 404, 500];
:reason: a very short description of what went wrong [might not be that useful though, use ``debug=true`` for more context];

Resources
=========

/v1/data/:year/:month/:key
--------------------------
/v1/:year/:month/:key
---------------------

Method: ``GET``
~~~~~~~~~~~~~~~

Retrieves all events/data withing a given month.

:status: * 200 ok
         * 404 not found
         * xxx error

:query string: * nan=purge: Removes all `nan/infinty` from the response;
               * nan=allow: The default, allow `nan/infinity` values to appear on the response;

/v1/data/:year/:month/:day/:key
-------------------------------

/v1/:year/:month/:day/:key
--------------------------

Method: ``GET``
~~~~~~~~~~~~~~~

Retrieves all events/data withing a given day.

:status: * 200 ok
         * 404 not found
         * xxx error

:query string: * nan=purge: Removes all `nan/infinty` from the response;
               * nan=allow: The default, allow `nan/infinity` values to appear on the response;

/v1/data/past24/:key
--------------------

/v1/past24/:key
---------------

Method: ``GET``
~~~~~~~~~~~~~~~

Retrieves data/events from the past 24 hours.

:status: * 200 ok
         * 404 not found
         * xxx error

:query string: * nan=purge: Removes all `nan/infinty` from the response;
               * nan=allow: The default, allow `nan/infinity` values to appear on the response;

/v1/data/pastweek/:key
----------------------

/v1/pastweek/:key
-----------------

Method: ``GET``
~~~~~~~~~~~~~~~

Retrieves data/events from the past week.

:status: * 200 ok
         * 404 not found
         * xxx error

:query string: * nan=purge: Removes all `nan/infinty` from the response;
               * nan=allow: The default, allow `nan/infinity` values to appear on the response;

/v1/data/:key
-------------

/v1/:key
--------

Method: ``GET``
~~~~~~~~~~~~~~~

Retrieves data/events within a given time range.

:status: * 200 ok
         * 404 not found
         * xxx error

:query string: * nan=purge: Removes all `nan/infinty` from the response;
               * nan=allow: The default, allow `nan/infinity` values to appear on the response;
               * start=TIMESPEC: The start time [UTC]. Make sure ``finish >= start``;
               * finish=TIMESPEC: The finish data [UTC];

TIMESPEC uses the the following *strftime* format: ::

  %Y%m%dT%H%M

Example::

  $ curl {endpoint}/v1/foobar?start=20120101T1430&finish=20120101T1500
  { "status": 200,
    "results": ...
  }

/v1/:key
--------

Method: ``POST``
~~~~~~~~~~~~~~~~

Inserts a new metric under this key. The body of the request must be a
valid json and the json must have the following keys:

:status: * 201 ok
         * 400 bad/missing required values;
         * xxx error

:parameters: * type: One of ``gauge``, ``counter``, ``derive``, ``absolute``
             * name: [optional] The name to store this metric. If this is provided, it must match the one given on the path;
             * value: The value to store under this key/timestamp;
             * timestamp: [optional] Unix timestamp [number of seconds since epoch];

You may also provide a list of metrics as long as theirs names match
the on given on the URL.

Examples: ::

  $ curl -X POST -d '{"type": "gauge", "value": 0.2}' {endpoint}/v1/foobar
  {"status": 201,
   "results": [{"name": "foobar", "timestamp": 1366549812, "type": "gauge", "value": 0.2}]
  }

.. _http put v1/data/key:

/v1/data/:key
-------------

Method: ``PUT``
~~~~~~~~~~~~~~~

*Deprecated: use /POST/*

Method: ``POST``
~~~~~~~~~~~~~~~~

Inserts a new data value under this key. The body of the request must
be a valid json, and the json must have the following keys:

:status: * 201 Ok
         * xxx error

:parameters: * name: [optional] The name to store this object. This must match the name given on the URL;
             * value: The value to store under this key/timestamp;
             * timestamp: [optional] Unix timestamp [number of seconds since epoch];

You may use this resource to store up to 8k bytes worth of data [in
the ``value`` field]. You may also provide a list of values [as long
as theirs names match the one given on the URL] in which case each
item of the list is subject to this limit.

Example: ::

  $ curl -X POST -d '{"value": :VALUE, "timestamp": 1352483918}' {endpoint}/v1/data/foobar
  { "status": 201,
    "results": [{"name": "foobar", "timestamp": 1352483918, "value": :VALUE}]
  }
