.. leela documentation master file, created by
   sphinx-quickstart on Wed Aug  1 14:40:54 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

===============
 Leela project
===============

Leela is a system that allows you to store, retrieve and monitor the
performance metrics of your systems in real-time using a variety of
protocols.

For data collection, currently you can use `collectd
<http://collectd.org>`_ or a :doc:`fairly simple text protocol over
UDP <users/udp>`. This gives you a decent coverage of standard
systems and applications at the same making it very easy to collect
custom metrics.

Data retrieval can be done using a :doc:`restful API <users/rest-api>`
which makes it easier to create dashboards, analyze historical data or
simply plot graphs in the browser.

You can even monitor real-time data using XMPP protocol. Simply
register a query and you will start receiving events in JSON as soon
as they are received by the server.

General
=======

* :doc:`Leela Architecture <general/architecture>`
* :doc:`Installing from Source <general/install-from-source>`
* :doc:`Installing the Debian Package <general/install-from-deb>`
* :doc:`Roadmap <general/roadmap>`

Administrators
==============

* :doc:`Configuring leela <sysadm/leela>`
* :doc:`Configuring cassandra <sysadm/cassandra>`
* :doc:`Configuring ejabberd <sysadm/ejabberd>`
* :doc:`Configuring redis <sysadm/redis>`
* :doc:`Monitoring and tuning <sysadm/monitoring-tuning>`

Users
=====

Writing
-------

* :doc:`Collectd interface <users/collectd>`
* :doc:`UDP interface <users/udp>`

Querying
--------

* :doc:`REST API <users/rest-api>`
* :doc:`Dashboard <users/dashboard>`

Monitoring
----------

* :doc:`XMPP interface <users/xmpp>`
* :doc:`DMPROC protocol <users/dmproc>`

Developers
----------

* :doc:`Javascript library <devel/js-api>`
* :doc:`Python library <devel/python-api>`
* :doc:`Ruby library <devel/ruby-api>`
* :doc:`Haskell library <devel/haskell-api>`

Changelog
=========

* https://github.com/locaweb/leela/blob/master/CHANGELOG

License
=======

APACHE 2.0

Author
======

* dgvncsz0f <dsouza@c0d3.xxx>

Contributors
============

* Juliano Martinez [former Author (v0.0.9)]
* Rodrigo Sampaio Vaz

.. toctree::
   :hidden:
   :glob:

   general/*
   users/index
   users/*
