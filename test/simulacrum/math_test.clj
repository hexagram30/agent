(ns simulacrum.math-test
  (:require [clojure.test :refer :all]
            [incanter.core :as matrix]
            [simulacrum.math :as math]))


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

(deftest test-round
  (is (= 0.0 (math/round 0)))
  (is (= 123.0 (math/round 123)))
  (is (= 123.0 (math/round 123 1)))
  (is (= 123.0 (math/round 123 2)))
  (is (= 0.1 (math/round 0.123 1)))
  (is (= 0.12 (math/round 0.123 2)))
  (is (= 0.123 (math/round 0.123 3)))
  (is (= 0.123 (math/round 0.1234 3)))
  (is (= 0.124 (math/round 0.1235 3)))
  (is (= 0.1235 (math/round 0.123456 4)))
  (is (= 0.12346 (math/round 0.123456 5))))

(deftest test-round-matrix
  (is (= [0.98 0.64 0.76 0.98 0.93] (math/round-matrix alice)))
  (is (= [[0.686 0.49  0.882 0.784 0.098]
          [0.448 0.32  0.576 0.512 0.064]
          [0.532 0.38  0.684 0.608 0.076]
          [0.686 0.49  0.882 0.784 0.098]
          [0.651 0.465 0.837 0.744 0.093]]
         (math/round-matrix (math/vmult alice dave))))
  (is (= [[0.69 0.49 0.88 0.78 0.1]
          [0.45 0.32 0.58 0.51 0.06]
          [0.53 0.38 0.68 0.61 0.08]
          [0.69 0.49 0.88 0.78 0.1]
          [0.65 0.47 0.84 0.74 0.09]]
         (math/round-matrix (math/vmult alice dave) 2))))

(deftest test-int-matrix
  (is (= [10 6 8 10 9] (math/int-matrix
                                      (matrix/mult 10
                                        (math/round-matrix alice 1)))))
  (is (= [[7 5 9 8 1]
          [4 3 6 5 1]
          [5 4 7 6 1]
          [7 5 9 8 1]
          [7 5 8 7 1]]
         (math/int-matrix
           (matrix/mult 10
             (math/round-matrix (math/vmult alice dave) 1))))))

(deftest test-vmult
  (is (= [[ 3.0  4.0]
          [12.0 16.0]]
         (matrix/to-vect (math/vmult frank gina)))))

(deftest test-get-scalar-distance
  (is (= 0.0
         (math/get-scalar-distance alice alice)))
  (is (= 0.6549045732013177
         (math/get-scalar-distance alice bob)))
  (is (= 1.7121915780659593
         (math/get-scalar-distance alice carol)))
  (is (= 0.9159148432032315
         (math/get-scalar-distance alice dave)))
  (is (= 1.1717081547894084
         (math/get-scalar-distance alice eve))))

(deftest test-get-matrix-difference
  (is (= [0.0 0.0 0.0 0.0 0.0]
         (math/round-matrix (math/get-matrix-difference dave dave))))
  (is (= [0.6 0.4 0.8 0.1 0.7]
         (math/round-matrix (math/get-matrix-difference dave eve)))))

(deftest test-get-inverted-matrix-difference
  (is (= [1.0 1.0 1.0 1.0 1.0]
         (math/round-matrix (math/get-inverted-matrix-difference eve eve))))
  (is (= [0.4 0.6 0.2 0.9 0.3]
         (math/round-matrix (math/get-inverted-matrix-difference dave eve)))))

(deftest test-normalize-matrix
  (is (= [[0.5 1.0]
          [1.5 2.0]]
         (math/round-matrix (math/normalize-matrix matrix-1))))
  (is (= [[0.5 1.0]
          [1.5 2.0]]
         (math/round-matrix (math/normalize-matrix matrix-1 :maxsize))))
  (is (= [[0.25 0.5]
          [0.75 1.0]]
         (math/round-matrix (math/normalize-matrix matrix-1 :largest))))
  (is (= [[0.333 0.667 1.0]
          [1.333 1.667 2.0]
          [2.333 2.667 3.0]]
         (math/round-matrix (math/normalize-matrix matrix-2))))
  (is (= [[0.111 0.222 0.333]
          [0.444 0.556 0.667]
          [0.778 0.889 1.0]]
         (math/round-matrix (math/normalize-matrix matrix-2 :largest)))))

(deftest test-get-normalized-matrix
  (is (= [[3.5  5.0]
          [7.5 11.0]]
         (math/round-matrix (math/get-normalized-matrix matrix-1 matrix-1))))
  (is (= [[3.5  5.0]
          [7.5 11.0]]
         (math/round-matrix
           (math/get-normalized-matrix matrix-1 matrix-1 :maxsize))))
  (is (= [[0.318 0.455]
          [0.682 1.0]]
         (math/round-matrix
           (math/get-normalized-matrix matrix-1 matrix-1 :largest)))))

(deftest test-compute-compatibility-matrix
  (is (= [[7.5  11.0]
          [30.0 44.0]]
         (math/round-matrix
           (math/compute-compatibility-matrix frank gina matrix-1))))
  (is (= [[7.5  11.0]
          [30.0 44.0]]
         (math/round-matrix
           (math/compute-compatibility-matrix
             frank gina matrix-1 :maxsize))))
  (is (= [[0.17 0.25]
          [0.682 1.0]]
         (math/round-matrix
           (math/compute-compatibility-matrix
             frank gina matrix-1 :largest)))))

(deftest test-get-transpose-average
  (let [couple (matrix/mmult (matrix/trans alice) bob)
        expected [[0.980 0.761 0.772 0.833 0.661]
                  [0.761 0.576 0.598 0.665 0.5465]
                  [0.772 0.598 0.608 0.658 0.524]
                  [0.833 0.665 0.658 0.686 0.5215]
                  [0.661 0.5465 0.524 0.5215 0.372]]
        result (math/get-transpose-average couple)]
    (is (= (matrix/matrix 0 5 5)
           (matrix/minus result expected)))))

