(ns hxgm30.agent.model.bigfive.core
  (:require
    [clojure.core.matrix :as matrix]
    [hxgm30.agent.const :as const]
    [hxgm30.agent.math :as math]))

(def domains
  {:O "Openness"
   :C "Conscientiousness"
   :E "Extraversion"
   :A "Agreeableness"
   :N "Neuroticism"
   :S "Stability"})

(def five-point-compatibility-matrix-model-1
  "An exploratory model using OCEAN."
  (matrix/matrix [[5 3 4 4 2]
                  [3 5 2 4 3]
                  [4 2 5 3 2]
                  [3 4 4 5 3]
                  [3 2 1 3 5]]))

(def five-point-compatibility-matrix-model-2
  "An exploratory model using OCEAN."
  (matrix/matrix [[5 3 4 4 2]
                  [2 5 3 4 1]
                  [4 2 5 3 2]
                  [3 4 4 5 3]
                  [3 2 1 3 5]]))

(def five-point-compatibility-matrix-model-3
  "An exploratory model using OCEAS."
  (matrix/matrix [[5 3 4 4 4]
                  [2 5 3 4 4]
                  [4 2 5 3 3]
                  [3 4 4 5 4]
                  [3 4 3 4 5]]))

(def five-point-compatibility-matrix
  "The columns of the compatibilty matrices follow the order of the OCEAS
  acronym:
    1) Openness, 2) Conscientiousness, 3) Extraversion, 4) Agreeableness,
    5) Stability.
  Similarly, the rows number in the same order.

  This function simply points to the matrix that provides the best default
  model for compatibilty.

  For more informtaion, see docs/compat.rst."
  five-point-compatibility-matrix-model-3)

(def signed-compatibility-matrix
  "Convert the compatibilty matrix to one whose values range from -2 to 2, with
  the neurtal value being 0."
  (matrix/sub five-point-compatibility-matrix
              const/mid-value))

(def normalized-compatibility-matrix
  "Convert the compatibilty matrix to one whose values have been normalized."
  (matrix/div five-point-compatibility-matrix
              (float const/max-value)))
