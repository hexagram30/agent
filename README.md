# hexagram30/agent

*Software agent emotional modeling, behavioural simulation, and AI for hexagramMUSH sentients (players, NPCs, animals, monsters, etc.)*

[![][logo]][logo-large]


## Big Five Short Inventory

The Big Five short inventory test displays 10 questions for the user to answer
and then tallies the results, displaying the five-trait break-down at the end.

```
$ ./scripts/bigfive-short.clj
```


## Big Five Long Inventory

The Big Five long inventory test displays 44 questions for the user to answer
and then tallies the results, displaying the five-trait break-down at the end.

```
$ ./scripts/bigfive-long.clj
```


## History

### Versions

* v0.6.0, 2018-08 - Brought project into hexagram30 org, renamed project to agent
* v0.5.0, 2013-11 - Migrated to Clojure, renamed project to clj-simulacrum
* v0.4.0, 2012-06 - Renamed project to innoth, code restructuring, added research papers
* v0.3.0, 2007-11 - Movement and interaction based on level of personality compatibility
* v0.2.0, 2006-02 - Renamed to "Emotional Modeling"; initial plans on
  game world integration
* v0.1.1, 2005-07 - Added code for developing games around the Rook
  world and related stories ("Rook Saga")
* v0.1.0, 2004-09 - Added code for personality simulation


### Project Background

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

1. The obvious application of this term is for what the library is trying to
   model rudimentarily: emotional states (which can then be used to inform
   behaviours);

1. At another level, simply to write this code, one must peer into the bowels
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


<!-- Named page links below: /-->

[logo]: https://raw.githubusercontent.com/hexagram30/resources/master/branding/logo/h30-logo-2-long-with-text-x695.png
[logo-large]: https://raw.githubusercontent.com/hexagram30/resources/master/branding/logo/h30-logo-2-long-with-text-x3440.png
[comp-event]: https://github.com/hexagram30/hexagramMUSH/blob/master/src/hexagram30/mush/components/event.clj
