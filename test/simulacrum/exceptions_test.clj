(ns simulacrum.exceptions-test
  (:require [clojure.test :refer :all]
            [simulacrum.exceptions :as exceptions]))


(deftest test-exception
  (is (thrown-with-msg?
        clojure.lang.ExceptionInfo
        #"oops"
        (throw (exceptions/exception "oops"))))
  (is (thrown-with-msg?
        clojure.lang.ExceptionInfo
        #"oops"
        (throw (exceptions/exception "oops" :type :wassup)))))

(deftest test-exception
  (is (thrown-with-msg?
        clojure.lang.ExceptionInfo
        #"bad parameter"
        (throw (exceptions/param-error "bad parameter")))))
