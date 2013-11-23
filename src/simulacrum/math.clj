(ns simulacrum.bigfive
  (:require [clojure.core.matrix :as matrix]
            [clojure.core.matrix.operators]
            [clojure.math.numeric-tower :refer [abs]])
  (:refer clojure.core.matrix.operators :rename
          {/ div
           * mult
           ** pow
           + add
           - sub
           == eql}))


(defn get-scalar-distance
  [pers-matrix-1 pers-matrix-2]
  "Get the scalar value for the distance between the two personality matrices.

  Note that the personality matrices are 1x5."
  (apply matrix/distance
         (map first [pers-matrix-1 pers-matrix-2])))

(defn get-matrix-difference
  [pers-matrix-1 pers-matrix-2]
  "Get the matrix for the difference between the two given matrices.

  Note that the personality matrices are 1x5 matrices and the resultant matrix
  is the same shape (1x5)."
  (matrix/emap abs
          (sub pers-matrix-1
               pers-matrix-2)))

(defn get-inverted-matrix-difference
  [pers-matrix-1 pers-matrix-2]
  "Get the matrix for the difference between the two given matrices.

  Note that the personality matrices are 1x5 matrices and the resultant matrix
  is the same shape (1x5)."
  (sub 1
       (get-matrix-difference
         pers-matrix-1
         pers-matrix-2)))

(defn normalize-matrix
  ([matrix-data]
   (normalize-matrix matrix :dimension))
  ([matrix-data normal-mode]
    (cond
      (= normal-mode :dimension)
        (div matrix-data (last (matrix/shape matrix-data)))
      (= normal-mode :largest)
        (div matrix-data (apply max (flatten matrix-data))))))

(defn get-normalized-matrix
  ""
  ([matrix-1 matrix-2]
   (get-normalized-matrix matrix-1 matrix-2 :dimension))
  ([matrix-1 matrix-2 normal-mode]
    (let [matrix (matrix/mmul matrix-1 matrix-2)]
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
     pers-matrix-1 pers-matrix-2 model :dimension))
  ([pers-matrix-1 pers-matrix-2 model normal-mode]
    (let [pers-combo (matrix/mmul (matrix/transpose pers-matrix-1) pers-matrix-2)
          compat-combo (matrix/mmul pers-combo model)]
      (normalize-matrix compat-combo normal-mode))))
