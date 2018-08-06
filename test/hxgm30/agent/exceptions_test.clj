(ns hxgm30.agent.exceptions-test
  (:require
    [clojure.test :refer :all]
    [hxgm30.agent.exceptions :as exceptions]))

(deftest test-exception
  (is (thrown-with-msg?
        clojure.lang.ExceptionInfo
        #"oops"
        (throw (exceptions/exception "oops"))))
  (is (thrown-with-msg?
        clojure.lang.ExceptionInfo
        #"oops"
        (throw (exceptions/exception "oops" :type :wassup)))))

(deftest test-param-error
  (is (thrown-with-msg?
        clojure.lang.ExceptionInfo
        #"bad parameter"
        (throw (exceptions/param-error "bad parameter")))))

(deftest test-range-error
  (is (thrown-with-msg?
        clojure.lang.ExceptionInfo
        #"bad range"
        (throw (exceptions/param-error "bad range")))))
