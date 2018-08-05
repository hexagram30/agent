(ns simulacrum.version-test
  (:require [clojure.test :refer :all]
            [simulacrum.version :as version]))


(deftest test-version
  (is (= 0 (version/version :major)))
  (is (= 5 (version/version :minor)))
  (is (= 0 (version/version :patch)))
  (is (= true (version/version :snapshot))))

(deftest test-version-str
  (is (= "v0.6.0-dev" version/version-str)))
