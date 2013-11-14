(ns simulacrum.bigfive-test
  (:require [clojure.test :refer :all]
            [simulacrum.bigfive :as bigfive]))


(deftest test-domains
  (is (= "Openness" (bigfive/domains :O)))
  (is (= "Conscientiousness" (bigfive/domains :C)))
  (is (= "Extraversion" (bigfive/domains :E)))
  (is (= "Agreeableness" (bigfive/domains :A)))
  (is (= "Neuroticism" (bigfive/domains :N))))

(deftest test-questions-base
  (is (= [:instructions :prefix]
         (sort (keys bigfive/questions-base)))))

(deftest test-questions-short
  (is (= [:instructions :prefix :questions :title]
         (sort (keys bigfive/questions-short))))
  (is (= 10 (count (bigfive/questions-short :questions)))))
