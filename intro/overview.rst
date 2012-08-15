==========
 Overview
==========

In short leela is an event processor and monitoring system.

As expected, leela has one core abstraction which is the *event*. It
is an object with an arbritrary name and a numeric value associated.

The processing of the events in leela is the possibility of applying
arbitrary functions over the data [e.g. *average* or computing the
*standard deviation*]. This can happen in two different phases:

Monitoring
==========

It is defined as the ability to applying a function to real time
events, as they arrive, and publishing this results to interested
parties.

As a example, consider the possibility of monitoring the average of
cpu usage and sending an email whenever this value gets over a certain
threshold.

Analyzes
========

Similarly, it is the possibility of applying a function over events,
but this time using stored data instead of real time data. As an
example, suppose you want to graph the 95 percentile of the
requests/second of your webserver for the past 6 months.
