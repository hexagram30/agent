(ns hxgm30.agent.model.alignment.core)

(def domains
  {:lg {:name "Righteous"
        :path "Integrity"
        :axes "Lawful Good"
        :focus "Conformity/Tradition and Benevolence"}
   :ng {:name "Humane"
        :path "Mercy"
        :axes "Neutral Good"
        :focus "Benevolence and Universalism"}
   :cg {:name "Transcendent"
        :path "Liberty"
        :axes "Chaotic Good"
        :focus "Universalism and Self-Direction"}
   :ln {:name "Orthodox"
        :path "Harmony"
        :axes "Lawful Neutral"
        :focus "Security and Conformity/Tradition"}
   :nn {:name "Pragmatic"
        :path "Equity"
        :axes "True Neutral"
        :focus "No specific focus"}
   :cn {:name "Autonomous"
        :path "Autonomy"
        :axes "Chaotic Neutral"
        :focus "Self-Direction and Stimulation"}
   :le {:name "Ascendent"
        :path "Ascendency"
        :axes "Lawful Evil"
        :focus "Power and Security"}
   :ne {:name "Ambitious"
        :path "Supremacy"
        :axes "Neutral Evil"
        :focus "Achievement and Power"}
   :ce {:name "Sybaritic"
        :path "Luxury"
        :axes "Chaotic Evil"
        :focus "Hedonism"}})

(def attracted
  {:lg #{:lg :ng :ln}
   :ng #{:lg :ng :cg :ln :nn :cn}
   :cg #{:ng :cg :nn :cn}
   :ln #{:lg :ng :ln :le}
   :nn #{:lg :ng :cg :ln :nn :cn :le :ne :ce}
   :cn #{:cg :nn :cn :ce}
   :le #{:ln :nn :le :ne}
   :ne #{:nn :cn :le :ne :ce}
   :ce #{:nn :cn :ne :ce}})

(defn attracted?
  ""
  [align to-other]
  (contains? (align attracted) to-other))

(def repulsed? (complement attracted?))

