(ns simulacrum.exceptions)


(defn exception [message & {:keys [type]}]
  (ex-info message
           {:type type
            :cause message}))

(defn param-error [message]
  (exception message :type :parameter-error))

(defn range-error [message]
  (exception message :type :range-error))
