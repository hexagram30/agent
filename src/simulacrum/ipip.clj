(ns simulacrum.ipip
  (:require [simulacrum.bigfive :refer [domains questions-base]]))


(def facets
  {:O1 "Imagination"
   :O2 "Artistic-Interests"
   :O3 "Emotionality"
   :O4 "Adventurousness"
   :O5 "Intellect"
   :O6 "Liberalism"
   :C1 "Self-Efficacy"
   :C2 "Orderliness"
   :C3 "Dutifulness"
   :C4 "Achievement-Striving"
   :C5 "Self-Discipline"
   :C6 "Cautiousness"
   :E1 "Friendliness"
   :E2 "Gregariousness"
   :E3 "Assertiveness"
   :E4 "Activity-Level"
   :E5 "Excitement-Seeking"
   :E6 "Cheerfulness"
   :A1 "Trust"
   :A2 "Morality"
   :A3 "Altruism"
   :A4 "Cooperation"
   :A5 "Modesty"
   :A6 "Sympathy"
   :N1 "Anxiety"
   :N2 "Anger"
   :N3 "Depression"
   :N4 "Self-Consciousness"
   :N5 "Immoderation"
   :N6 "Vulnerability"})

(def questions-short
  (conj
    questions-base
    {:title "IPIP NEO-PI-R Facet Scales Short Inventory"
     :questions
      [

       ]}))
