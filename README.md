# hexagram30/agent

*Software agent emotional modeling, behavioural simulation, and AI for hexagramMUSH sentients (players, NPCs, animals, monsters, etc.)*

[![][logo]][logo-large]


## About

The agent library aims to provide everything needed in-game to:

* describe the personal attributes (strengths and weaknesses) of sentients
* determine the natural compatibilities of sentients (attraction/aversion)
* peovide a means of determining (re)action gradients
* creating and using decision trees
* creating and using problem solvers

The functionality inherited from earlier versions of this library has focused on
personality traits and interactions between personalities. As such, significant
progress has been made in that direction; the remaining features have yet to be
addressed and will require a fair chunk of work.


## Bonus Materials

### Big Five Short Inventory

The Big Five short inventory test displays 10 questions for the user to answer
and then tallies the results, displaying the five-trait break-down at the end.

```
$ lein big-five-short
```


## Other Inventories

A long version of the big five inventory is in the works, as well as both long
and short of the IPIP inventory.


## Release Notes

* v0.6.1, 2018-08 - Removed old Python code
* v0.6.0, 2018-08 - Brought project into hexagram30 org, renamed project to agent
* v0.5.0, 2013-11 - Migrated to Clojure, renamed project to clj-simulacrum
* v0.4.0, 2012-06 - Renamed project to innoth, code restructuring, added research papers
* v0.3.0, 2007-11 - Movement and interaction based on level of personality compatibility
* v0.2.0, 2006-02 - Renamed to "Emotional Modeling"; initial plans on
  game world integration
* v0.1.1, 2005-07 - Added code for developing games around the Rook
  world and related stories ("Rook Saga")
* v0.1.0, 2004-09 - Added code for personality simulation


## License

Copyright © 2018, Hexagram30

Copyright © 2004-2013, Duncan McGreggor

Apache License, Version 2.0


<!-- Named page links below: /-->

[logo]: https://raw.githubusercontent.com/hexagram30/resources/master/branding/logo/h30-logo-2-long-with-text-x695.png
[logo-large]: https://raw.githubusercontent.com/hexagram30/resources/master/branding/logo/h30-logo-2-long-with-text-x3440.png
[comp-event]: https://github.com/hexagram30/hexagramMUSH/blob/master/src/hexagram30/mush/components/event.clj
