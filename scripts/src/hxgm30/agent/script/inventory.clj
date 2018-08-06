(ns hxgm30.agent.script.inventory
  (:require
    [clojure.string :as string]
    [hxgm30.agent.const :as const]
    [hxgm30.agent.exceptions :as exceptions]
    [hxgm30.agent.model.bigfive.core :refer [domains]]
    [hxgm30.agent.model.bigfive.inventory]
    [hxgm30.agent.model.ipip.inventory]
    [hxgm30.agent.script.inventory.ipip :as ipip-generator]
    [hxgm30.agent.script.util :as util])
  (:gen-class))

(defn display-title
  [questions]
  (let [title (:title questions)
        heading (util/mult-str "=" (count title))]
  (println (str heading))
  (println (str title))
  (println (str heading))
  (println)))

(defn display-instructions
  [questions]
  (println (:instructions questions)))

(defn get-answer
  [prefix question]
  (let [raw-question (string/lower-case (:question question))
        str-question (str "\""
                      prefix
                      raw-question
                      (if-not (string/ends-with? raw-question ".")
                        ".\" "
                        "\" "))
        mini-instruction (str "(Enter one of "
                              (vec (range 1 6))
                              "; 1=disagree, 5=agree) ")]
    (let [answer (util/input (str str-question mini-instruction))]
      (cond
        (:reversed? question)
          [(:domain-key question) (- 6 answer)]
        :else
          [(:domain-key question) answer]))))

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

(defn -run-inventory
  [questions]
  (display-title questions)
  (display-instructions questions)
  (println)
  (display-score
    (process-results
      (map #(get-answer (:prefix questions) %)
           (questions :questions)))))

(defn run-inventory
  ([questions-model]
    (run-inventory questions-model {}))
  ([questions-model opts]
    (if (:generate? opts)
      (case (:type opts)
        :ipip (-run-inventory
               (merge questions-base
                      questions-model
                      (ipip-generator/generate-questions (:variant opts)))))
      (-run-inventory
       (merge questions-base questions-model)))))

(defn get-inventory-fn
  [test-type test-variant]
  (case
    :bigfive run-inventory
    :ipip #(run-inventory % {:generate? true
                             :type test-type
                             :variant test-variant})))

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
   * short

  Additionally, the `ipip` test type may take `full` as a parameter, which
  will result in a test with all 305 questions."
  [test-type test-variant]
  (let [inventory-fn (get-inventory-fn (keyword test-type)
                                       (keyword test-variant))]
    (-> "hxgm30.agent.model.%s.inventory/questions-%s"
        (format test-type test-variant)
        symbol
        resolve
        var-get
        inventory-fn)))

(defn -main
  [& args]
  (util/clear-screen)
  (apply run args)
  (util/exit))
