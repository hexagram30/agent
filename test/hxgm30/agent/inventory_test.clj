(ns hxgm30.agent.inventory-test
  (:require [clojure.test :refer :all]
            [hxgm30.agent.inventory :as inventory]))

(deftest test-run-no-short-no-long
  (is (thrown-with-msg?
        clojure.lang.ExceptionInfo
        #"One of ':short true' or ':long true' must be passed to this function"
        (inventory/run :bigfive))))

(deftest test-get-groups
  (let [data [[:E 5] [:A 2] [:C 3] [:N 2] [:O 1]
              [:E 1] [:A 4] [:C 1] [:N 1] [:O 4]]]
    (is (= {:E [[:E 5] [:E 1]], :A [[:A 2] [:A 4]], :C [[:C 3] [:C 1]],
            :N [[:N 2] [:N 1]], :O [[:O 1] [:O 4]]}
           (inventory/get-groups data)))))

(deftest test-gather-subgroups
  (let [data [:E [[:E 5] [:E 1]]]]
    (is (= [5 1]
           (inventory/gather-subgroups data)))))

(deftest test-average-tuple
  (is (= 3.0 (inventory/average-tuple [1 5])))
  (is (= 2.5 (inventory/average-tuple [1 4])))
  (is (= 3.0 (inventory/average-tuple [2 4]))))

(deftest test-process-results
  (let [data [[:E 5] [:A 2] [:C 3] [:N 2] [:O 1]
              [:E 5] [:A 2] [:C 3] [:N 2] [:O 1]]]
    (is (= {:E 5.0, :A 2.0, :C 3.0, :N 2.0, :O 1.0}
           (inventory/process-results data))))
  (let [data [[:E 5] [:A 2] [:C 3] [:N 2] [:O 1]
              [:E 1] [:A 4] [:C 1] [:N 1] [:O 4]]]
    (is (= {:E 3.0, :A 3.0, :C 2.0, :N 1.5, :O 2.5}
           (inventory/process-results data)))))
