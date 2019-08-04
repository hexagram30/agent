(ns hxgm30.agent.model.alignment.core-test
  (:require
   [clojure.test :refer :all]
   [hxgm30.agent.model.alignment.core :as alignment]))

(deftest attracted?
  (is (= true (alignment/attracted? :lg :lg)))
  (is (= false (alignment/attracted? :lg :cg)))
  (is (= true (alignment/attracted? :lg :ln)))
  (is (= true (alignment/attracted? :ln :lg)))
  (is (= false (alignment/attracted? :lg :nn)))
  (is (= true (alignment/attracted? :nn :lg))))

(deftest repulsed?
  (is (= false (alignment/repulsed? :lg :lg)))
  (is (= true (alignment/repulsed? :lg :cg)))
  (is (= false (alignment/repulsed? :lg :ln)))
  (is (= false (alignment/repulsed? :ln :lg)))
  (is (= true (alignment/repulsed? :lg :nn)))
  (is (= false (alignment/repulsed? :nn :lg))))
