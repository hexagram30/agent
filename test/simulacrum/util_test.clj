(ns simulacrum.util-test
  (:require [clojure.test :refer :all]
            [simulacrum.util :as util]))


(deftest test-get-last-line
  (let [test-data "This is some
                  multi-line
                  text.
                  Enjoy!"]
    (is (= "Enjoy!" (util/get-last-line test-data)))))

(deftest test-in?
  (is (= true (util/in? [1 2] 1)))
  (is (= true (util/in? [1 2] 2)))
  (is (= false (util/in? [1 2] 0)))
  (is (= false (util/in? [1 2] 3))))

(deftest test-check-input
  (is (= 1 (util/check-input 1)))
  (is (= 3 (util/check-input 3)))
  (is (= 5 (util/check-input 5)))
  (is (= 5 (util/check-input 5)))
  (is (thrown-with-msg?
        clojure.lang.ExceptionInfo
        #"Input must be between 1 and 5"
        (util/check-input 0)))
  (is (thrown-with-msg?
        clojure.lang.ExceptionInfo
        #"Input must be between 1 and 5"
        (util/check-input 6))))
