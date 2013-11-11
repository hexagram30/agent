(ns simulacrum.util
  (:require [clojure.string :as string]
            [simulacrum.exceptions :as exceptions]))


(defn display [data]
  (.print (System/out) data))

(defn exit []
  (display (str \newline "Exiting ... " \newline))
  (System/exit 0))

(defn clear-screen []
  (display "\u001b[2J")
  (display "\u001B[0;0f"))

(defn beep []
  (clear-screen)
  (display (char 7))
  (clear-screen))

(defn in?
  "Given a sequence and a potential element of that sequence, determine if it
  is, in fact, part of that sequence."
  [sequence item]
  (if (empty? sequence)
    false
    (reduce
      #(or %1 %2)
      (map
        #(= %1 item)
        sequence))))

(defn check-input [input]
  (let [valid-range (range 1 6)]
    (cond
      (in? valid-range input)
        input
      :else (throw
              (exceptions/range-error
                (str "Input must be between " (first valid-range) " and "
                     (last valid-range)))))))

(defn input [prompt]
  (display prompt)
  (check-input (read-line)))

(defn get-last-line [text]
  (string/trim
    (last
      (string/split text #"\n"))))

