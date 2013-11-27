(ns simulacrum.math
  (:require [incanter.core :as matrix]
            [incanter.stats :as stats]
            [clojure.math.numeric-tower :as tower]))


(defn round
  ([n]
   (round n 3))
  ([n precision]
   (let [prec-mult (tower/expt 10 precision)]
     (/ (tower/round (* n prec-mult))
        (float prec-mult)))))

(defn round-matrix
  ([matrix-data]
   (round-matrix matrix-data 3))
  ([matrix-data precision]
    (matrix/matrix-map
      #(round % precision)
      (matrix/to-vect matrix-data))))

(defn int-matrix [matrix-data]
  (matrix/matrix-map
    int
    (matrix/to-vect matrix-data)))

(defn vmult [vector-1 vector-2]
  (matrix/mmult (matrix/trans vector-1) vector-2))

(defn get-scalar-distance
  [pers-matrix-1 pers-matrix-2]
  "Get the scalar value for the Euclidian distance between the two personality
  matrices.

  Note that the personality matrices are 1x5."
  (stats/euclidean-distance pers-matrix-1 pers-matrix-2))

(defn get-matrix-difference
  [pers-matrix-1 pers-matrix-2]
  "Get the matrix for the difference between the two given matrices.

  Note that the personality matrices are 1x5 matrices and the resultant matrix
  is the same shape (1x5)."
  (matrix/matrix-map tower/abs
               (matrix/minus pers-matrix-1
                             pers-matrix-2)))

(defn get-inverted-matrix-difference
  [pers-matrix-1 pers-matrix-2]
  "Get the matrix for the difference between the two given matrices.

  Note that the personality matrices are 1x5 matrices and the resultant matrix
  is the same shape (1x5)."
  (matrix/minus 1
                (get-matrix-difference pers-matrix-1
                                       pers-matrix-2)))

(defn normalize-matrix
  "Given a matrix, normalize it either by the largest value in the shape vector
  (:maxsize) or by the largest element in the matrix (:largest).

  'normal-mode' is the method used to select the normalization value. If the
  value of 'normal-mode' is :rank, the matrix rank is used to normalize the
  values in the matrix. If it is :largest, the largest value of the matrix is
  given as the rank."
  ([matrix-data]
   (normalize-matrix matrix-data :maxsize))
  ([matrix-data normal-mode]
    (cond
      (= normal-mode :maxsize)
        (matrix/div matrix-data (last (matrix/dim matrix-data)))
      (= normal-mode :largest)
        (matrix/div matrix-data (apply max (flatten matrix-data))))))

(defn get-normalized-matrix
  "Given two matrices, multiply them and normaize the result.

  'normal-mode' is the method used to select the normalization value. If the
  value of 'normal-mode' is :rank, the matrix rank is used to normalize the
  values in the matrix. If it is :largest, the largest value of the matrix is
  given as the rank."
  ([matrix-1 matrix-2]
   (get-normalized-matrix matrix-1 matrix-2 :maxsize))
  ([matrix-1 matrix-2 normal-mode]
    (let [matrix (matrix/mmult matrix-1 matrix-2)]
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
     pers-matrix-1 pers-matrix-2 model :maxsize))
  ([pers-matrix-1 pers-matrix-2 model normal-mode]
    (let [pers-combo (matrix/mmult (matrix/trans pers-matrix-1) pers-matrix-2)
          compat-combo (matrix/mmult pers-combo model)]
      (normalize-matrix compat-combo normal-mode))))

(defn get-transpose-average
  [matrix-data]
  "Add the given matrix to its transpose and then divide by two.

  This is useful for forming diagonal matrices from personality matrix
  multiplication results."
  (matrix/div (matrix/plus
                (matrix/trans matrix-data)
                matrix-data)
              2))



