(ns hxgm30.agent.math-test
  (:require
    [clojure.core.matrix :as matrix]
    [clojure.test :refer :all]
    [hxgm30.agent.math :as math]))

(def alice
  (matrix/matrix [[0.98 0.64 0.76 0.98 0.93]]))

(def bob
  (matrix/matrix [[1.0 0.9 0.8 0.7 0.4]]))

(def carol
  (matrix/matrix [[0.02 0.36 0.24 0.02 0.07]]))

(def dave
  (matrix/matrix [[0.7 0.5 0.9 0.8 0.1]]))

(def eve
  (matrix/matrix [[0.1 0.9 0.1 0.7 0.8]]))

(def frank (matrix/matrix [[1 4]]))

(def gina (matrix/matrix [[3 4]]))

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
  (is (= (matrix/matrix [[0.98 0.64 0.76 0.98 0.93]])
         (math/round-matrix alice)))
  (is (= (matrix/matrix [[1.0,0.6,0.8,1.0,0.9]])
         (math/round-matrix alice 1)))
  (is (= (matrix/matrix [[1.0,1.0,1.0,1.0,1.0]])
         (math/round-matrix alice 0)))
  (is (= (matrix/matrix
          [[0.686 0.49  0.882 0.784 0.098]
           [0.448 0.32  0.576 0.512 0.064]
           [0.532 0.38  0.684 0.608 0.076]
           [0.686 0.49  0.882 0.784 0.098]
           [0.651 0.465 0.837 0.744 0.093]])
         (math/round-matrix (math/vector-mul alice dave))))
  (is (= (matrix/matrix
          [[0.69 0.49 0.88 0.78 0.1]
           [0.45 0.32 0.58 0.51 0.06]
           [0.53 0.38 0.68 0.61 0.08]
           [0.69 0.49 0.88 0.78 0.1]
           [0.65 0.47 0.84 0.74 0.09]])
         (math/round-matrix (math/vector-mul alice dave) 2))))

(deftest test-int-matrix
  (is (= (matrix/matrix [[10 6 8 10 9]])
         (math/int-matrix
          (matrix/mul
           10 (math/round-matrix alice 1)))))
  (is (= (matrix/matrix [[7 5 9 8 1]
                         [4 3 6 5 1]
                         [5 4 7 6 1]
                         [7 5 9 8 1]
                         [7 5 8 7 1]])
         (math/int-matrix
          (matrix/mul
           10 (math/round-matrix
               (math/vector-mul alice dave)
               1))))))

(deftest test-vector-mul
  (is (= (matrix/matrix
          [[0.98 0.882 0.784 0.686 0.392]
           [0.64 0.576 0.512 0.448 0.256]
           [0.76 0.684 0.608 0.532 0.304]
           [0.98 0.882 0.784 0.686 0.392]
           [0.93 0.837 0.744 0.651 0.372]])
         (math/round-matrix (math/vector-mul alice bob)))))

(deftest test-scalar-distance
  (is (= 0.0
         (math/scalar-distance alice alice)))
  (is (= 0.6549045732013177
         (math/scalar-distance alice bob)))
  (is (= 1.7121915780659593
         (math/scalar-distance alice carol)))
  (is (= 0.9159148432032315
         (math/scalar-distance alice dave)))
  (is (= 1.1717081547894084
         (math/scalar-distance alice eve))))

(deftest test-matrix-distance
  (is (= (matrix/matrix [[0.0 0.0 0.0 0.0 0.0]])
         (math/round-matrix (math/matrix-distance dave dave))))
  (is (= (matrix/matrix [[0.6 0.4 0.8 0.1 0.7]])
         (math/round-matrix (math/matrix-distance dave eve)))))

(deftest test-matrix-closeness
  (is (= (matrix/matrix [[1.0 1.0 1.0 1.0 1.0]])
         (math/round-matrix (math/matrix-closeness eve eve))))
  (is (= (matrix/matrix [[0.4 0.6 0.2 0.9 0.3]])
         (math/round-matrix (math/matrix-closeness dave eve)))))

(deftest test-normalize-matrix
  (is (= (matrix/matrix [[0.25 0.5]
                         [0.75 1.0]])
         (math/round-matrix (math/normalize-matrix matrix-1))))
  (is (= (matrix/matrix [[0.5 1.0]
                         [1.5 2.0]])
         (math/round-matrix (math/normalize-matrix matrix-1 :max-shape))))
  (is (= (matrix/matrix [[0.25 0.5]
                         [0.75 1.0]])
         (math/round-matrix (math/normalize-matrix matrix-1 :max-val))))
  (is (= (matrix/matrix [[0.111 0.222 0.333]
                         [0.444 0.556 0.667]
                         [0.778 0.889 1.0]])
         (math/round-matrix (math/normalize-matrix matrix-2))))
  (is (= (matrix/matrix [[0.333 0.667 1.0]
                         [1.333 1.667 2.0]
                         [2.333 2.667 3.0]])
         (math/round-matrix (math/normalize-matrix matrix-2 :max-shape)))))

(deftest test-normalize-matrices
  (is (= (matrix/matrix
          [[0.06 0.25]
           [0.56 1.0]])
         (math/round-matrix (math/normalize-matrices matrix-1 matrix-1)
          2)))
  (is (= (matrix/matrix
          [[0.5 2.0]
           [4.5 8.0]])
         (math/round-matrix
          (math/normalize-matrices matrix-1 matrix-1 :max-shape)
          2)))
  (is (= (matrix/matrix
          [[0.06 0.25]
           [0.56 1.0]])
         (math/round-matrix
          (math/normalize-matrices matrix-1 matrix-1 :max-val)
          2))))

(deftest test-compute-compatibility-matrix
  (is (= (matrix/matrix
          [[0.05 0.13]
           [0.56 1.0]])
         (math/round-matrix
           (math/compute-compatibility-matrix frank gina matrix-1)
           2)))
  (is (= (matrix/matrix
          [[1.5 4.0]
           [18.0 32.0]])
         (math/round-matrix
          (math/compute-compatibility-matrix
           frank gina matrix-1 :max-shape)
          2)))
  (is (= (matrix/matrix
          [[0.05 0.13]
           [0.56 1.0]])
         (math/round-matrix
          (math/compute-compatibility-matrix
           frank gina matrix-1 :max-val)
          2))))

(deftest test-get-transpose-average
  (let [couple (math/vector-mul alice bob)
        expected [[0.980 0.761 0.772 0.833 0.661]
                  [0.761 0.576 0.598 0.665 0.5465]
                  [0.772 0.598 0.608 0.658 0.524]
                  [0.833 0.665 0.658 0.686 0.5215]
                  [0.661 0.5465 0.524 0.5215 0.372]]
        result (math/get-transpose-average couple)]
    (is (= (matrix/zero-matrix 5 5)
           (math/round-matrix (matrix/sub result expected))))))
