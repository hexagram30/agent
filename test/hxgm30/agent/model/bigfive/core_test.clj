(ns hxgm30.agent.model.bigfive.core-test
  (:require
    [clojure.core.matrix :as matrix]
    [clojure.test :refer :all]
    [hxgm30.agent.math :as math]
    [hxgm30.agent.model.bigfive.core :as bigfive]))

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
  (is (= (matrix/matrix
          [[5 3 4 4 2]
           [3 5 2 4 3]
           [4 2 5 3 2]
           [3 4 4 5 3]
           [3 2 1 3 5]])
         (math/int-matrix
          bigfive/five-point-compatibility-matrix-model-1))))

(deftest test-five-point-compatibility-matrix-model-2
  (is (= (matrix/matrix
          [[5 3 4 4 2]
           [2 5 3 4 1]
           [4 2 5 3 2]
           [3 4 4 5 3]
           [3 2 1 3 5]])
         (math/int-matrix
          bigfive/five-point-compatibility-matrix-model-2))))

(deftest test-five-point-compatibility-matrix-model-3
  (is (= (matrix/matrix
          [[5 3 4 4 4]
           [2 5 3 4 4]
           [4 2 5 3 3]
           [3 4 4 5 4]
           [3 4 3 4 5]])
         (math/int-matrix
          bigfive/five-point-compatibility-matrix-model-3))))

(deftest test-five-point-compatibility-matrix
  (is (= bigfive/five-point-compatibility-matrix-model-3
         bigfive/five-point-compatibility-matrix)))

(deftest test-signed-compatibility-matrix
  (is (= (matrix/matrix
          [[ 2   0   1   1   1]
           [-1   2   0   1   1]
           [ 1  -1   2   0   0]
           [ 0   1   1   2   1]
           [ 0   1   0   1   2]])
         (math/int-matrix
          bigfive/signed-compatibility-matrix))))

(deftest test-normalized-compatibility-matrix
  (is (= (matrix/matrix
          [[1.0 0.6 0.8 0.8 0.8]
           [0.4 1.0 0.6 0.8 0.8]
           [0.8 0.4 1.0 0.6 0.6]
           [0.6 0.8 0.8 1.0 0.8]
           [0.6 0.8 0.6 0.8 1.0]])
    (math/round-matrix
     bigfive/normalized-compatibility-matrix
     1))))
