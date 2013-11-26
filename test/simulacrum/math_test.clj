(ns simulacrum.math-test
  (:require [clojure.test :refer :all]
            [clojure.core.matrix :as matrix]
            [clojure.core.matrix.operators]
            [simulacrum.math :as math])
  (:refer clojure.core.matrix.operators :rename
          {/ div
           * mult
           ** pow
           + add
           - sub
           == eql}))


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

(def frank [[1 4]])

(def gina [[3 4]])

(def matrix-1
  (matrix/matrix [[1 2]
                  [3 4]]))

(def matrix-2
  (matrix/matrix [[1 2 3]
                  [4 5 6]
                  [7 8 9]]))

(deftest test-get-scalar-distance
  (is (= 0.0
         (math/get-scalar-distance alice alice)))
  (is (= 0.6549045732013177
         (math/get-scalar-distance alice bob)))
  (is (= 1.7121915780659593
         (math/get-scalar-distance alice carol)))
  (is (= 0.9159148432032314
         (math/get-scalar-distance alice dave)))
  (is (= 1.1717081547894084
         (math/get-scalar-distance alice eve))))

(deftest test-get-matrix-difference
  (is (= [[0.0M 0.0M 0.0M 0.0M 0.0M]]
         (math/get-matrix-difference dave dave)))
  (is (= [[0.6M 0.4M 0.8M 0.1M 0.7M]]
         (math/get-matrix-difference dave eve))))

(deftest test-get-inverted-matrix-difference
  (is (= [[1.0M 1.0M 1.0M 1.0M 1.0M]]
         (math/get-inverted-matrix-difference eve eve)))
  (is (= [[0.4M 0.6M 0.2M 0.9M 0.3M]]
         (math/get-inverted-matrix-difference dave eve))))

(deftest test-normalize-matrix
  (is (= [[1/2 1]
          [3/2 2]]
         (math/normalize-matrix matrix-1)))
  (is (= [[1/2 1]
          [3/2 2]]
         (math/normalize-matrix matrix-1 :maxsize)))
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
         (math/get-normalized-matrix matrix-1 matrix-1 :maxsize)))
  (is (= [[7/22 5/11]
          [15/22 1]]
         (math/get-normalized-matrix matrix-1 matrix-1 :largest))))

(deftest test-compute-compatibility-matrix
  (is (= [[15/2 11]
          [30 44]]
         (math/compute-compatibility-matrix frank gina matrix-1)))
  (is (= [[15/2 11]
          [30 44]]
         (math/compute-compatibility-matrix
           frank gina matrix-1 :maxsize)))
  (is (= [[15/88 1/4]
          [15/22 1]]
         (math/compute-compatibility-matrix
           frank gina matrix-1 :largest))))

(deftest test-get-transpose-average
  (let [couple (matrix/mmul (matrix/transpose alice) bob)
        expected [[0.980 0.761 0.772 0.833 0.661]
                  [0.761 0.576 0.598 0.665 0.5465]
                  [0.772 0.598 0.608 0.658 0.524]
                  [0.833 0.665 0.658 0.686 0.5215]
                  [0.661 0.5465 0.524 0.5215 0.372]]
        result (math/get-transpose-average couple)]
    (is (= (matrix/new-matrix 5 5) (sub result expected)))))

