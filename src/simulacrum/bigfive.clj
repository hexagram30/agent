(ns simulacrum.bigfive)


(def attributes
  {:O "Openness"
   :C "Conscientiousness"
   :E "Extraversion"
   :A "Agreeableness"
   :N "Neuroticism"})

(def questions-base
  {:instructions (str "Answer each question below by providing a number "
                      "between 1 and 5. The values " \newline
                      "of the integers have the following "
                      "meanings:" \newline
                      \tab "* 5 is 'Agree Strongly'" \newline
                      \tab "* 4 is 'Agree a Little'" \newline
                      \tab "* 3 is 'Neutral'" \newline
                      \tab "* 2 is 'Disagree a Little'" \newline
                      \tab "* 1 is 'Disagree Strongly'. " \newline \newline
                      "How well do the following statements describe your "
                      "personality?")
   :prefix "I see myself as someone who "})

(def questions-short
  (conj
    questions-base
    {:title "Five Factor Model (Big Five) Short Inventory"
     :questions [{:question "is reserved"
                  :type :E
                  :reversed? true}
                 {:question "is generally trusting"
                  :type :A
                  :reversed? false}
                 {:question "tends to be lazy"
                  :type :C
                  :reversed? true}
                 {:question "is relaxed, handles stress well"
                  :type :N
                  :reversed? true}
                 {:question "has few artistic interests"
                  :type :O
                  :reversed? true}
                 {:question "is outgoing, sociable"
                  :type :E
                  :reversed? false}
                 {:question "tends to find fault with others"
                  :type :A
                  :reversed? true}
                 {:question "does a thorough job"
                  :type :C
                  :reversed? false}
                 {:question "gets nervous easily"
                  :type :N
                  :reversed? false}
                 {:question "has an active imagination"
                  :type :O
                  :reversed? false}]}))

(def questions-long
  (conj
    questions-base
    {}))


