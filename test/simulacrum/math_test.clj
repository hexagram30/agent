(ns simulacrum.math-test
  (:require [clojure.test :refer :all]
            [clojure.core.matrix :as matrix]
            [simulacrum.math :as math]))


(def person-1
  (matrix/matrix [[0.7M 0.5M 0.9M 0.8M 0.1M]]))

(def person-2
  (matrix/matrix [[0.1M 0.9M 0.1M 0.7M 0.8M]]))

(def person-3 [[1 4]])

(def person-4 [[3 4]])

(def matrix-1
  (matrix/matrix [[1 2]
                  [3 4]]))

(def matrix-2
  (matrix/matrix [[1 2 3]
                  [4 5 6]
                  [7 8 9]]))

(deftest test-get-scalar-distance
  (is (= 0.0
         (math/get-scalar-distance person-1 person-1)))
  (is (= 1.2884098726725126
         (math/get-scalar-distance person-1 person-2))))

(deftest test-get-matrix-difference
  (is (= [[0.0M 0.0M 0.0M 0.0M 0.0M]]
         (math/get-matrix-difference person-1 person-1)))
  (is (= [[0.6M 0.4M 0.8M 0.1M 0.7M]]
         (math/get-matrix-difference person-1 person-2))))

(deftest test-get-inverted-matrix-difference
  (is (= [[1.0M 1.0M 1.0M 1.0M 1.0M]]
         (math/get-inverted-matrix-difference person-1 person-1)))
  (is (= [[0.4M 0.6M 0.2M 0.9M 0.3M]]
         (math/get-inverted-matrix-difference person-1 person-2))))

(deftest test-normalize-matrix
  (is (= [[1/2 1]
          [3/2 2]]
         (math/normalize-matrix matrix-1)))
  (is (= [[1/2 1]
          [3/2 2]]
         (math/normalize-matrix matrix-1 :dimension)))
  (is (= [[1/4 1/2]
          [3/4 1]]
         (math/normalize-matrix matrix-1 :largest)))
  (is (= [[1/3 2/3 1]
          [4/3 5/3 2]
          [7/3 8/3 3]]
         (math/normalize-matrix matrix-2)))
  (is (= [[1/9 2/9 1/3]
          [4/9 5/9 2/3]
          [7/9 8/9 1]]
         (math/normalize-matrix matrix-2 :largest))))

(deftest test-get-normalized-matrix
  (is (= [[7/2 5]
          [15/2 11]]
         (math/get-normalized-matrix matrix-1 matrix-1)))
  (is (= [[7/2 5]
          [15/2 11]]
         (math/get-normalized-matrix matrix-1 matrix-1 :dimension)))
  (is (= [[7/22 5/11]
          [15/22 1]]
         (math/get-normalized-matrix matrix-1 matrix-1 :largest))))

(deftest test-compute-compatibility-matrix
  (is (= [[15/2 11]
          [30 44]]
         (math/compute-compatibility-matrix person-3 person-4 matrix-1)))
  (is (= [[15/2 11]
          [30 44]]
         (math/compute-compatibility-matrix
           person-3 person-4 matrix-1 :dimension)))
  (is (= [[15/88 1/4]
          [15/22 1]]
         (math/compute-compatibility-matrix
           person-3 person-4 matrix-1 :largest))))
