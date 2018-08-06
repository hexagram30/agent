(ns hxgm30.agent.model.ipip.core-test
  (:require
    [clojure.core.matrix :as matrix]
    [clojure.test :refer :all]
    [hxgm30.agent.math :as math]
    [hxgm30.agent.model.ipip.core :as ipip]))

(deftest test-facets
  (is (= "Imagination" (ipip/facets :O1)))
  (is (= "Orderliness" (ipip/facets :C2)))
  (is (= "Assertiveness" (ipip/facets :E3)))
  (is (= "Cooperation" (ipip/facets :A4)))
  (is (= "Immoderation" (ipip/facets :N5)))
  (is (= "Indefatigability" (ipip/facets :S6)))
  (is (= 36 (count ipip/facets))))
