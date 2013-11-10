~~~~~~~~~~~~~~
clj-simulacrum
~~~~~~~~~~~~~~

A Clojure library for exploring perosnality and emotional modeling via software 
agents in simulated populations.


Installation
============

Usage
=====


Project History
===============

This project was originally started in 2004 as "Emotional Modeling" or
"Emotional Models" (depending on which names were already taken in which hosted
code repository service).  Recent work on other code bases (game-related ones 
such as Myriad Worlds, Peloid Server) caused interest to be resumed in this
particular code base. However, there is a long legacy of code in this project 
and a fresh start was in order, although still using the Python programming
language.

After creating the "cweþan" project whose ultimate intended use is for NPCs in
text-based games, another Old English name seemed appropriate. After some poking
around in dictionaries, "innoþ" was chosen.

Innoþ can mean "the inner part of the body", "the inside", "breast, heart,
stomach, womb, belly", or in reference to feeling, emotion, etc. It is cognate
to Old High and Low German words for viscera: "innethron" and "innod,"
respectively.

This is appropriate enough, at two levels:

#. The obvious application of this term is for what the library is trying to
   model rudimentarily: emotional states (which can then be used to inform
   behaviours);

#. At another level, simply to write this code, one must peer into the bowels
   of human nature, dig into its guts, cut it down to basic principles. This
   task is rather encompassing and is at the heart of any code that might be
   written to simulate what this inward-looking process might reveal.

Not much progress was made for meany reasons, not the least of which was the
relative difficulty to run massively parallel simulations efficiently in
Python. This, however, was just the sort of which the Actor model (e.g., the
Erlang programming language) has proved quite adept at.

With the addition of `Parallel Universe`_'s `Pulsar open source project`_ in
the spring of 2013, the Clojure ecosystem now has an Actor model library with
light-weight thread support (called "fibers" which only use ~400 bytes each).
As such, now seems like a perfect opportunity to update this library, switch
to Clojure, and take advantage of these features for personality simulation
in the large.


.. Links
.. =====

.. _Parallel Universe: http://paralleluniverse.co/
.. _Pulsar open source project: https://github.com/puniverse/pulsar
