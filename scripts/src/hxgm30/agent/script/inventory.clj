(ns hxgm30.agent.script.inventory
  (:require
    [hxgm30.agent.const :as const]
    [hxgm30.agent.exceptions :as exceptions]
    [hxgm30.agent.model.bigfive.core :refer [domains]]
    [hxgm30.agent.model.bigfive.inventory]
    [hxgm30.agent.model.ipip.inventory]
    [hxgm30.agent.script.util :as util])
  (:gen-class))

(defn display-title
  [questions]
  (let [title (questions :title)
        heading (util/mult-str "=" (count title))]
  (println (str heading))
  (println (str title))
  (println (str heading))
  (println)))

(defn display-instructions
  [questions]
  (println (questions :instructions)))

(defn get-answer
  [prefix question]
  (println (str "\"" prefix (question :question) ".\""))
  (let [answer (util/input (str "Enter one of " (vec (range 1 6)) " "))]
    (println)
    (cond
      (question :reversed?)
        [(question :domain-key) (- 6 answer)]
      :else
        [(question :domain-key) answer])))

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
  "Given a group, determine the average and associate it with its domain."
  [group]
  [(first group) (average-tuple (gather-subgroups group))])

(defn process-results
  [results]
  (into {}
        (map
          group-average
          (get-groups results))))

(defn display-score
  [averages]
  (let [title "Inventory Results"
        heading (util/mult-str "=" (count title))]
    (println (str \newline heading))
    (println (str title))
    (println (str heading \newline))
    (doseq [[key value] averages]
      (println
        (str \tab (domains key) ": " value)))))

(def questions-base
  {:instructions (str "Answer each question below by providing a number "
                      "between " const/min-value
                      " and " const/max-value ". The values " \newline
                      "of the integers have the following meanings:" \newline
                      \tab "* 5 is 'Agree Strongly'" \newline
                      \tab "* 4 is 'Agree a Little'" \newline
                      \tab "* 3 is 'Neutral'" \newline
                      \tab "* 2 is 'Disagree a Little'" \newline
                      \tab "* 1 is 'Disagree Strongly'. " \newline \newline
                      "How well do the following statements describe your "
                      "personality?")
   :prefix "I see myself as someone who "})

(defn run-inventory
  [questions-model]
  (let [questions (merge questions-base questions-model)
        prefix (questions :prefix)]
    (display-title questions)
    (display-instructions questions)
    (println)
    (display-score
      (process-results
        (map #(get-answer prefix %) (questions :questions))))))

(defn run
  "The required positional parameter (not one of the named parameters) needs to
  be a keyword that maps to a defined module for personality traits.

  Right now, the list of supported personality trait frameworks are the
  following:
    * bigfive
    * ipip
  As string values, these are the legal values for the first argument.

  Legal values for the second argument are the string values:
   * long
   * short"
  [test-type test-variant]
  (-> "hxgm30.agent.model.%s.inventory/questions-%s"
      (format test-type test-variant)
      symbol
      resolve
      var-get
      run-inventory))

(defn -main
  [& args]
  (util/clear-screen)
  (apply run args)
  (util/exit))
