~~~~~~~~~~~~~~
clj-simulacrum
~~~~~~~~~~~~~~

.. contents:: Table of Contents


A Clojure library for exploring perosnality and emotional modeling via software
agents in simulated populations.


Installation
============

``clj-simulacrum`` depends upon `incanter`_, which has a non-standard source
build. If you don't have ``incanter`` already installed, you will need to
install it. We provide a conveient means of doing this with a ``make`` target
in our ``Makefile``.

If you do have ``incanter`` installed, you can skip this "Installation" step
and move right to the "Project Inclusion" step below. You project will download
``clj-simulacrum`` from `Clojars`_ when you run ``lein deps`` on your project.

For those that don't have ``incanter`` installed:

.. code:: bash

    $ git clone git@github.com:oubiwann/clj-simulacrum.github
    $ cd clj-simulacrum
    $ make deps

This will download ``incanter`` and then build it into your ``~/.m2`` directory.
After that, you will be able to run ``clj-simulacrum``.


Project Inclusion
=================

You can add ``clj-simulacrum`` to your ``project.clj`` with the following:

.. code:: clojure

    (defproject your-project "1.2.3"
      ...
      :dependencies [[org.clojure/clojure "1.5.1"]
                     [...]
                     [clj-simulacrum "0.1.0"]]
      ...)

You can then use it in your project like so:

.. code:: clojure

    (ns your-project.client
      (:require [simulacrum :as sim]))

Or from the REPL:

.. code:: clojure

    (require '[simulacrum :as sim])


Library Usage
=============

TBD

.. code:: clojure

    TBD


Running the Scripts
===================

This project provides a small set of scripts that may be useful for you. They
are described below.


Big Five Short Inventory
------------------------

The Big Five short inventory test displays 10 questions for the user to answer
and then tallies the results, displaying the five-trait break-down at the end.

To run:

.. code:: bash

  $ ./scripts/bigfive-short.clj


Big Five Long Inventory
-----------------------

The Big Five long inventory test displays 44 questions for the user to answer
and then tallies the results, displaying the five-trait break-down at the end.

To run:

.. code:: bash

  $ ./scripts/bigfive-long.clj


History
=======


Versions
--------

* 0.1 - Dummy release, containing only versioning info and no real code.


Project Background
------------------

This project was originally started in 2004 as "Emotional Modeling" or
"Emotional Models" (depending on which names were already taken in which hosted
code repository service). The purpose of that code was to attempt simulation
of agents with minimal personality definitions.

Later work on other code bases (game-related ones, such as Myriad Worlds,
Peloid Server) caused interest to be resumed in this particular code base.
However, there is a long legacy of code in this project and a fresh start was
in order. This was started, although it continued to use the Python programming
language.

After creating the "cweþan" project whose ultimate intended use was for NPCs in
text-based games, another Old English name seemed appropriate. After some poking
around in dictionaries, "innoþ" was chosen.

Innoþ can mean "the inner part of the body", "the inside", "breast, heart,
stomach, womb, belly", or in reference to feeling, emotion, etc. It is cognate
to Old High and Low German words for viscera: "innethron" and "innod,"
respectively.

This was appropriate enough, at two levels:

#. The obvious application of this term is for what the library is trying to
   model rudimentarily: emotional states (which can then be used to inform
   behaviours);

#. At another level, simply to write this code, one must peer into the bowels
   of human nature, dig into its guts, cut it down to basic principles. This
   task is rather encompassing and is at the heart of any code that might be
   written to simulate what this inward-looking process might reveal.

Not much progress was made for many reasons, not the least of which was the
relative difficulty to run massively parallel simulations efficiently in
Python. This, however, was just the sort of which the Actor model (e.g., the
Erlang programming language) has proved quite adept at.

With the addition of `Parallel Universe`_'s `Pulsar open source project`_ in
the spring of 2013, the Clojure ecosystem now has an Actor model library with
light-weight thread support (called "fibers" which only use ~400 bytes each).
As such, now seems like a perfect opportunity to update this library, switch
to Clojure, and take advantage of these features for personality simulation
in the large.

Finally, the project was renamed clj-simulacrum, the Python code was moved into
the sandbox directory, and a fresh start was made in the Clojure programming
language.


.. Links
.. =====

.. _Clojars: https://clojars.org/clj-simulacrum
.. _incanter: https://github.com/liebke/incanter
.. _Parallel Universe: http://paralleluniverse.co/
.. _Pulsar open source project: https://github.com/puniverse/pulsar
