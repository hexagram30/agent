(ns simulacrum.bigfive-test
  (:require [clojure.test :refer :all]
            [simulacrum.bigfive :as bigfive]))


(deftest test-attributes
  (is (= "Openness" (bigfive/attributes :O)))
  (is (= "Conscientiousness" (bigfive/attributes :C)))
  (is (= "Extraversion" (bigfive/attributes :E)))
  (is (= "Agreeableness" (bigfive/attributes :A)))
  (is (= "Neuroticism" (bigfive/attributes :N))))

(deftest test-questions-base
  (is (= [:instructions :prefix]
         (sort (keys bigfive/questions-base)))))

(deftest test-questions-short
  (is (= [:instructions :prefix :questions :title]
         (sort (keys bigfive/questions-short))))
  (is (= 10 (count (bigfive/questions-short :questions)))))
