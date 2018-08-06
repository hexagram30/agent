(ns hxgm30.agent.math
  (:require
    [clojure.core.matrix :as matrix]
    [clojure.math.numeric-tower :as math]))

(defn round
  ([n]
   (round n 3))
  ([n precision]
   (let [prec-mult (math/expt 10 precision)]
     (/ (math/round (* n prec-mult))
        (float prec-mult)))))

(defn round-matrix
  ([matrix-data]
   (round-matrix matrix-data 3))
  ([matrix-data precision]
    (matrix/emap
      #(round % precision)
      matrix-data)))

(defn int-matrix [matrix-data]
  (matrix/emap
    int
    matrix-data))

(defn transpose-vector
  [matrix-data]
  (matrix/matrix (partition 1 (matrix/as-vector matrix-data))))

(defn vector-mul
  [v1 v2]
  (matrix/mmul (transpose-vector v1) v2))

(defn scalar-distance
  "Get the scalar value for the Euclidian distance between the two personality
  matrices.

  Note that the personality matrices are 1x5."
  [pers-matrix-1 pers-matrix-2]
  (matrix/distance (matrix/as-vector pers-matrix-1)
                   (matrix/as-vector pers-matrix-2)))

(defn matrix-distance
  "Get the matrix for the element-wise distance between corresponding elements
  of the two given matrices.

  Note that the personality matrices are 1x5 matrices and the resultant matrix
  is the same shape (1x5).

  Assumes normalized matrices."
  [pers-matrix-1 pers-matrix-2]
  (matrix/emap math/abs
               (matrix/sub pers-matrix-1
                           pers-matrix-2)))

(defn matrix-closeness
  "Get the matrix for the element-wise 'closeness' between corresponding elements
  of the two given matrices. This is the arithmatic inverse of matrix-distance.

  Assumes normalized matrices."
  [pers-matrix-1 pers-matrix-2]
  (matrix/sub 1
              (matrix-distance pers-matrix-1
                               pers-matrix-2)))

(defn normalize-matrix
  "Given a matrix, normalize it either by the largest value in the shape vector
  (:maxsize) or by the largest element in the matrix (:largest).

  'normal-mode' is the method used to select the normalization value. If the
  value of 'normal-mode' is :rank, the matrix rank is used to normalize the
  values in the matrix. If it is :largest, the largest value of the matrix is
  given as the rank."
  ([matrix-data]
   (normalize-matrix matrix-data :max-val))
  ([matrix-data normal-mode]
    (cond
      (= normal-mode :max-val)
      (matrix/div matrix-data (matrix/maximum matrix-data))

      (= normal-mode :max-shape)
      (matrix/div matrix-data (apply max (matrix/shape matrix-data))))))

(defn normalize-matrices
  "Given two matrices, multiply them and normaize the result.

  'normal-mode' is the method used to select the normalization value. If the
  value of 'normal-mode' is :rank, the matrix rank is used to normalize the
  values in the matrix. If it is :largest, the largest value of the matrix is
  given as the rank."
  ([matrix-1 matrix-2]
   (normalize-matrices matrix-1 matrix-2 :max-val))
  ([matrix-1 matrix-2 normal-mode]
    (let [matrix (matrix/mul matrix-1 matrix-2)]
      (normalize-matrix matrix normal-mode))))

(defn compute-compatibility-matrix
  "Multiply the personality matrices by each other and then the result by the
  compatibilty matrix (the given model).

  'normal-mode' is the method used to select the normalization value. If the
  value of 'normal-mode' is :rank, the matrix rank is used to normalize the
  values in the matrix. If it is :largest, the largest value of the matrix is
  given as the rank."
  ([pers-matrix-1 pers-matrix-2 model]
   (compute-compatibility-matrix
     pers-matrix-1 pers-matrix-2 model :max-val))
  ([pers-matrix-1 pers-matrix-2 model normal-mode]
    (let [pers-combo (vector-mul pers-matrix-1 pers-matrix-2)
          compat-combo (matrix/mul pers-combo model)]
      (normalize-matrix compat-combo normal-mode))))

(defn get-transpose-average
  "Add the given matrix to its transpose and then divide by two.

  This is useful for forming diagonal matrices from personality matrix
  multiplication results."
  [matrix-data]
  (matrix/div (matrix/add
                (matrix/transpose matrix-data)
                matrix-data)
              2))
