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
    {:title "Five Factor Model (Big Five) Long Inventory"
     :questions [{:number 1
                  :question "is talkative"
                  :type :E
                  :reversed? false}
                 {:number 2
                  :question "tends to find fault with others"
                  :type :A
                  :reversed? true}
                 {:number 3
                  :question "XXX"
                  :type :E
                  :reversed? true}
                 {:number 4
                  :question "XXX"
                  :type :E
                  :reversed? true}
                 {:number 5
                  :question "XXX"
                  :type :E
                  :reversed? true}
                 {:number 6
                  :question "XXX"
                  :type :E
                  :reversed? true}
                 {:number 7
                  :question "XXX"
                  :type :A
                  :reversed? false}
                 {:number 8
                  :question "XXX"
                  :type :E
                  :reversed? true}
                 {:number 9
                  :question "XXX"
                  :type :E
                  :reversed? true}
                 {:number 10
                  :question "XXX"
                  :type :E
                  :reversed? true}
                 {:number 11
                  :question "XXX"
                  :type :E
                  :reversed? true}
                 {:number 12
                  :question "XXX"
                  :type :A
                  :reversed? true}
                 {:number 13
                  :question "XXX"
                  :type :E
                  :reversed? true}
                 {:number 14
                  :question "XXX"
                  :type :E
                  :reversed? true}
                 {:number 15
                  :question "XXX"
                  :type :E
                  :reversed? true}
                 {:number 16
                  :question "XXX"
                  :type :E
                  :reversed? true}
                 {:number 17
                  :question "XXX"
                  :type :A
                  :reversed? false}
                 {:number 18
                  :question "XXX"
                  :type :E
                  :reversed? true}
                 {:number 19
                  :question "XXX"
                  :type :E
                  :reversed? true}
                 {:number 20
                  :question "XXX"
                  :type :E
                  :reversed? true}
                 {:number 21
                  :question "XXX"
                  :type :E
                  :reversed? true}
                 {:number 22
                  :question "XXX"
                  :type :A
                  :reversed? false}
                 {:number 23
                  :question "XXX"
                  :type :E
                  :reversed? true}
                 {:number 24
                  :question "XXX"
                  :type :E
                  :reversed? true}
                 {:number 25
                  :question "XXX"
                  :type :E
                  :reversed? true}
                 {:number 26
                  :question "XXX"
                  :type :E
                  :reversed? true}
                 {:number 27
                  :question "XXX"
                  :type :A
                  :reversed? true}
                 {:number 28
                  :question "XXX"
                  :type :E
                  :reversed? true}
                 {:number 29
                  :question "XXX"
                  :type :E
                  :reversed? true}
                 {:number 30
                  :question "XXX"
                  :type :E
                  :reversed? true}
                 {:number 31
                  :question "XXX"
                  :type :E
                  :reversed? true}
                 {:number 32
                  :question "XXX"
                  :type :A
                  :reversed? false}
                 {:number 33
                  :question "XXX"
                  :type :E
                  :reversed? true}
                 {:number 34
                  :question "XXX"
                  :type :E
                  :reversed? true}
                 {:number 35
                  :question "XXX"
                  :type :E
                  :reversed? true}
                 {:number 36
                  :question "XXX"
                  :type :E
                  :reversed? true}
                 {:number 37
                  :question "XXX"
                  :type :A
                  :reversed? true}
                 {:number 38
                  :question "XXX"
                  :type :E
                  :reversed? true}
                 {:number 39
                  :question "XXX"
                  :type :E
                  :reversed? true}
                 {:number 40
                  :question "XXX"
                  :type :E
                  :reversed? true}
                 {:number 41
                  :question "XXX"
                  :type :E
                  :reversed? true}
                 {:number 42
                  :question "XXX"
                  :type :A
                  :reversed? false}
                 {:number 43
                  :question "XXX"
                  :type :E
                  :reversed? true}
                 {:number 44
                  :question "XXX"
                  :type :E
                  :reversed? true}
     ]}))


