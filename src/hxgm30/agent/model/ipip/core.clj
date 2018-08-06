(ns hxgm30.agent.model.ipip.core
  (:require
    [clojure.core.matrix :as matrix]
    [hxgm30.agent.const :as const]
    [hxgm30.agent.model.bigfive.core :refer [domains]]))

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
   :N6 "Vulnerability"
   :S1 "Serenity"
   :S2 "Good-Will"
   :S3 "Contentment"
   :S4 "Confidence"
   :S5 "Moderation"
   :S6 "Indefatigability"})

(def thirty-point-compatibility-matrix-model-1
  "The problems observed with this model were:
    * "
  (matrix/matrix
    [[]]))

(def thirty-point-compatibility-matrix-model-2
  "This model exhibits the following properties:
    * "
  (matrix/matrix
    [[]]))

(def thirty-point-compatibility-matrix
  "The columns of the compatibilty matrices follow the order of the OCEAN
  acronym:
    1) Openness, 2) Conscientiousness, 3) Extraversion, 4) Agreeableness,
    5) Neuroticism.
  Similarly, the rows number in the same order.

  This function simply points to the matrix that provides the best default
  model for compatibilty.
  For more informtaion, see docs/compat.rst."
  thirty-point-compatibility-matrix-model-2)

(def signed-compatibility-matrix
  "Convert the compatibilty matrix to one whose values range from -2 to 2, with
  the neurtal value being 0."
  (matrix/sub thirty-point-compatibility-matrix const/mid-value))

(def normalized-compatibility-matrix
  "Convert the compatibilty matrix to one whose values have been normalized."
  (matrix/emap
    float
    (matrix/div thirty-point-compatibility-matrix const/max-value)))
