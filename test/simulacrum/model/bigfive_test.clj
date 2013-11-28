(ns simulacrum.model.bigfive-test
  (:require [clojure.test :refer :all]
            [incanter.core :as matrix]
            [simulacrum.math :as math]
            [simulacrum.model.bigfive :as bigfive]))


(def person-1 [[]])

(def person-2 [[]])

(deftest test-domains
  (is (= "Openness" (bigfive/domains :O)))
  (is (= "Conscientiousness" (bigfive/domains :C)))
  (is (= "Extraversion" (bigfive/domains :E)))
  (is (= "Agreeableness" (bigfive/domains :A)))
  (is (= "Neuroticism" (bigfive/domains :N)))
  (is (= "Stability" (bigfive/domains :S))))

(deftest test-five-point-compatibility-matrix-model-1
  (is (= [[5 3 4 4 2]
          [3 5 2 4 3]
          [4 2 5 3 2]
          [3 4 4 5 3]
          [3 2 1 3 5]] (math/int-matrix
                         bigfive/five-point-compatibility-matrix-model-1))))

(deftest test-five-point-compatibility-matrix-model-2
  (is (= [[5 3 4 4 2]
          [2 5 3 4 1]
          [4 2 5 3 2]
          [3 4 4 5 3]
          [3 2 1 3 5]] (math/int-matrix
                         bigfive/five-point-compatibility-matrix-model-2))))

(deftest test-five-point-compatibility-matrix-model-3
  (is (= [[5 3 4 4 4]
          [2 5 3 4 4]
          [4 2 5 3 3]
          [3 4 4 5 4]
          [3 4 3 4 5]] (math/int-matrix
                         bigfive/five-point-compatibility-matrix-model-3))))

(deftest test-five-point-compatibility-matrix
  (is (= bigfive/five-point-compatibility-matrix-model-3
         bigfive/five-point-compatibility-matrix)))

(deftest test-signed-compatibility-matrix
  (is (= [[ 2   0   1   1   1]
          [-1   2   0   1   1]
          [ 1  -1   2   0   0]
          [ 0   1   1   2   1]
          [ 0   1   0   1   2]] (math/int-matrix
                                  bigfive/signed-compatibility-matrix))))

(deftest test-normalized-compatibility-matrix
  (is (= [[1.0M 0.6M 0.8M 0.8M 0.8M]
          [0.4M 1.0M 0.6M 0.8M 0.8M]
          [0.8M 0.4M 1.0M 0.6M 0.6M]
          [0.6M 0.8M 0.8M 1.0M 0.8M]
          [0.6M 0.8M 0.6M 0.8M 1.0M]]
    (matrix/to-vect
      bigfive/normalized-compatibility-matrix))))

(deftest test-questions-base
  (is (= [:instructions :prefix]
         (sort (keys bigfive/questions-base)))))

(deftest test-questions-short
  (is (= [:instructions :prefix :questions :title]
         (sort (keys bigfive/questions-short))))
  (is (= 10 (count (bigfive/questions-short :questions)))))

(deftest test-questions-long
  )



