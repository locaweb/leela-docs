.. leela documentation master file, created by
   sphinx-quickstart on Wed Aug  1 14:40:54 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

===============
 Leela project
===============

Leela is an distributed, scalable, event processor and monitoring
system.

It allows you to publish data using many different protocols. For
instance, you are able to store data using a simle text protocol over
:doc:`UDP <fe/udp>`, or using a :doc:`Restful API <fe/udp>` or even
using the `collectd network plugin
<https://collectd.org/wiki/index.php/Plugin:Network>`_ [#]_.

Once the data has been published Leela will store information up to a
second time resolution. The historical information is then available
to you through the :doc:`Restful API <fe/http>`, which should allow
one to easily analyze information or create rich dashboards.

You may also monitor events in real-time using the :doc:`XMPP
<fe/xmpp>` interface. It allows you to watch a subset of the events as
soon as they are published or to transform them in a more suitable
representation, using a very simple but powerful :doc:`stream
processing language <dmproc/dmproc>`.

Using
=====

Storing data
------------

* :doc:`UDP interface <fe/udp>`
* :ref:`HTTP interface <http put v1/data/key>`

.. toctree::
  :hidden:

  fe/udp

Retrieving data
---------------

* :doc:`HTTP interface <fe/http>`
* :doc:`XMPP interface <fe/xmpp>`
* :doc:`Stream processing language <dmproc/dmproc>`

.. toctree::
  :hidden:

  fe/http
  fe/xmpp
  dmproc/dmproc

Changelog
=========

* https://raw.github.com/locaweb/leela-server/master/CHANGELOG

Help
====

Having problems, questions or suggestions? Don't hesitate to reach us!

* IRC(freenode): #leela;

* leela@listadev.email.locaweb.com.br;

.. [#] Work in progress!
