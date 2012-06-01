~~~~
TODO
~~~~


Emotional Modeling
==================

At each tick of the simulation clock, each agent must be able to process the
following information:

* current state name or ID

* stress-based coping mode (Omega_i where i = 1,5)

* currently afforded transitions and what actions might cause those state
  transitions (a_nm in A(Omega))

* subjective desires for each state based on 11 pairs of emotional scales
  summed into an overall utility score, U

Using all of this information, the agent must select a decision style Phi and
process the information in order to produce a best repsonse (BR) that maximizes
expected, discounted rewards or utilities in the current iteration of the world.

Utility may be thought of as the simple summation of all positive and negative
emotions for an action leading to a state.

After emotional intensity is obtained for each emotion, they need to be summed
and averaged over the 11 ranges.


Python Components
=================

emotion module receives input from the perception module

the perception module is moderated by the physiology module (python components?)

Things need to be componentized... we need to be able to do something like
create an environment class that incorporates a metric class (measurement), a
class for handling movement in the environment, a class for handling actions in
the environment.

We need to look at the differences between actions that an agent can do and
actions that can be performed in an environment.

We need to examine relative positioning vs. absolute positioning.

What do the agents know about their own location?

Memory of agent vs. attributes of objects... or, put a better way, how much do
agents know of the structure of themselves? Do they have access to object
attributes? My vote: no. Agent knowledge/awareness needs to sit behind a
"firewall", without access to object attributes.
