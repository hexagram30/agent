(ns hxgm30.agent.repl
  (:require
    [clojure.core.matrix :as matrix]
    [hxgm30.agent.math :as math]
    [hxgm30.agent.model.bigfive :as bigfive]
    [hxgm30.agent.model.ipip :as ipip]))

(def alice
  (matrix/matrix [[0.98M 0.64M 0.76M 0.98M 0.93M]]))

(def bob
  (matrix/matrix [[1.0M 0.9M 0.8M 0.7M 0.4M]]))

(def carol
  (matrix/matrix [[0.02M 0.36M 0.24M 0.02M 0.07M]]))

(def dave
  (matrix/matrix [[0.7M 0.5M 0.9M 0.8M 0.1M]]))

(def eve
  (matrix/matrix [[0.1M 0.9M 0.1M 0.7M 0.8M]]))

(def frank (matrix/matrix [[1 4]]))

(def gina (matrix/matrix [[3 4]]))

(def matrix-1
  (matrix/matrix [[1 2]
                  [3 4]]))

(def matrix-2
  (matrix/matrix [[1 2 3]
                  [4 5 6]
                  [7 8 9]]))
