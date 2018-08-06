## Project History

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

There are several interesting options in the Clojure work for this: everything
from Akka to Quasar/Pulsar and even Clojang (Erlang's JInterface wrapped
for Clojure). Even more, by using Clojure, the massive Java ecosystem was made
available.

In the next iteration, the project was renamed clj-simulacrum, the Python code
was moved into the sandbox directory, and a fresh start was made using the Clojure
programming language.

Finally, the Clojure version was moved into the hexagram30 family of libraries
in support of building interactive, multi-user, text-based worlds complete with
simulated sentients of all forms.
