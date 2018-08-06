(ns hxgm30.agent.model.bigfive.inventory-test
  (:require
    [clojure.test :refer :all]
    [hxgm30.agent.model.bigfive.inventory :as inventory]))

(deftest test-questions-short
  (is (= [:questions :title]
         (sort (keys inventory/questions-short))))
  (is (= 10 (count (inventory/questions-short :questions)))))
