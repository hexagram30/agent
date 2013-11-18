(ns simulacrum.util
  (:require [clojure.java.io :as io]
            [clojure.data.json :as json]
            [clojure.string :as string]
            [clj-http.client :as client]
            [net.cgrand.enlive-html :as html]
            [simulacrum.exceptions :as exceptions]
            [simulacrum.version :as version]))


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

(defn mult-str [string amount]
  (string/join (repeat amount string)))

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
  (let [valid-range (range 1 6)
        input (Integer. input)]
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

(defn make-dirs [path]
  (io/make-parents
    (str path "null")))

(def user-agent
  (str
    "clj-simulacrum "
    version/version-str
    " (https://github.com/oubiwann/clj-simulacrum)"))

(def headers {:headers {"User-Agent" user-agent}})

(defn fetch-url [url & {:keys [headers] :or {headers headers}}]
  (html/html-snippet
    ((client/get url headers) :body)))

(defn remove-spaces-and-newlines [text]
  (string/replace text #"\s+\n\s+" " "))

(defn remove-trailing-non-ascii [text]
  (string/replace
    (string/replace
      (string/replace
        text
        #"^\n\s+$" "")
      (str (char 160)) "")
    (str (char 65533)) ""))

(defn clean-string [text]
  (remove-trailing-non-ascii
    (remove-spaces-and-newlines text)))

(defn import-lite []
  (map (fn[x] {:question (x :question)
               :domain-key (keyword (x :domain-key))
               :facet-key (keyword (x :facet-id))
               :reversed? (:x :reversed?)})
       (json/read-str
         (slurp "target/json/ipip-newo-pi-r.json")
         :key-fn keyword)))


