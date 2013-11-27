(ns simulacrum.ipip-test
  (:require [clojure.test :refer :all]
            [incanter.core :as matrix]
            [simulacrum.ipip :as ipip]
            [simulacrum.math :as math]))


(deftest test-facets
  (is (= "Imagination" (ipip/facets :O1)))
  (is (= "Orderliness" (ipip/facets :C2)))
  (is (= "Assertiveness" (ipip/facets :E3)))
  (is (= "Cooperation" (ipip/facets :A4)))
  (is (= "Immoderation" (ipip/facets :N5)))
  (is (= "Indefatigability" (ipip/facets :S6)))
  (is (= 36 (count ipip/facets))))
