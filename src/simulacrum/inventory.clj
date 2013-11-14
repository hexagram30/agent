(ns simulacrum.inventory
  (:require [simulacrum.bigfive :as bigfive]
            [simulacrum.exceptions :as exceptions]
            [simulacrum.util :as util]))


(defn display-title [questions]
  (let [title (questions :title)
        heading (util/mult-str "=" (count title))]
  (util/display (str heading \newline))
  (util/display (str title \newline))
  (util/display (str heading \newline))
  (util/display \newline)))

(defn display-instructions [questions]
  (util/display (questions :instructions))
  (util/display \newline))

(defn get-answer [prefix question]
  (util/display (str "\"" prefix (question :question) ".\"" \newline))
  (let [answer (util/input (str "Enter one of " (into [] (range 1 6)) " "))]
    (util/display \newline)
    (cond
      (question :reversed?)
        [(question :type) (- 6 answer)]
      :else
        [(question :type) answer])))

(defn get-groups
  "This is used when processing the results."
  [results]
  (group-by first results))

(defn gather-subgroups
  "This is used when processing the results."
  [subgroup]
  (map second (second subgroup)))

(defn average-tuple
  "This is used when processing the results."
  [tuple]
  (/ (reduce + tuple) (float (count tuple))))

(defn group-average
  "Given a group, determine the average and associate it with its type."
  [group]
  [(first group) (average-tuple (gather-subgroups group))])

(defn process-results [results]
  (into {}
        (map
          group-average
          (get-groups results))))

(defn display-score [averages]
  (let [title "Inventory Results"
        heading (util/mult-str "=" (count title))]
    (util/display (str heading \newline))
    (util/display (str title \newline))
    (util/display (str heading \newline \newline))
    (doseq [[key value] averages]
      (util/display
        (str \tab (bigfive/domains key) ": " value \newline)))))

(defn -run-inventory [questions]
  (let [prefix (questions :prefix)]
    (display-title questions)
    (display-instructions questions)
    (util/display \newline)
    (display-score
      (process-results
        (map #(get-answer prefix %) (questions :questions))))))

(defn run-inventory
  "The required positional parameter (not one of the named parameters) needs to
  be a keyword that maps to a defined module for personality traits. For
  instance, if simulacrum.bigfive is defined (and it is) and you wanted to run
  the inventory for it, you'd pass :bigfive.

  Right now, the list of supported personality trait frameworks are the
  following:
    * :bigfive
    * :ipip

  One of ':short true' or ':long true' must be passed to this function."
  [type-keyword & {:keys [short long]}]
  (let [type (name type-keyword)]
      (cond
        (not (nil? short))
          (-run-inventory (eval (symbol type "questions-short")))
        (not (nil? long))
          (-run-inventory (eval (symbol type "questions-long")))
        :else (throw
                (exceptions/param-error
                  (util/get-last-line ((meta #'run-inventory) :doc)))))))
