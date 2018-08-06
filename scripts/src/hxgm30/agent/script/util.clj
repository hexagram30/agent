(ns hxgm30.agent.script.util
  (:require
    [clj-http.client :as client]
    [clojure.data.json :as json]
    [clojure.edn :as edn]
    [clojure.java.io :as io]
    [clojure.string :as string]
    [hxgm30.agent.exceptions :as exceptions]
    [net.cgrand.enlive-html :as html]))

(def valid-range (range 1 6))
(def valid-range-err-msg
  (str "Input must be between "
       (first valid-range)
       " and "
       (last valid-range)))

(defn exit
  []
  (println (str \newline "Exiting ... "))
  (System/exit 0))

(defn clear-screen
  []
  (print "\u001b[2J")
  (print "\u001B[0;0f"))

(defn beep
  []
  (clear-screen)
  (print (char 7))
  (clear-screen))

(defn mult-str
  [string amount]
  (string/join (repeat amount string)))

(defn in?
  "Given a sequence and a potential element of that sequence, determine if it
  is, in fact, part of that sequence."
  [sequence item]
  (if (empty? sequence)
    false
    (contains? (set sequence) item)))

(defn check-input
  [input]
  (let [input (Integer. input)]
    (if (in? valid-range input)
      input
      (throw
        (exceptions/range-error valid-range-err-msg)))))

(defn input
  [prompt]
  (print prompt)
  (flush)
  (try
    (check-input (read-line))
    (catch clojure.lang.ExceptionInfo ex
      (println (.getMessage ex))
      (input prompt))
    (catch java.lang.NumberFormatException ex
      (println valid-range-err-msg)
      (input prompt))))

(defn get-last-line
  [text]
  (string/trim
    (last
      (string/split text #"\n"))))

(defn make-dirs [path]
  (io/make-parents
    (str path "null")))

(def user-agent
  (str
    "hexagram30/agent "
    "0.6.1-SNAPSHOT "
    "(https://github.com/hexagram30/agent)"))

(def ua-headers {:headers {"User-Agent" user-agent}})

(defn fetch-url
  [url & {:keys [headers]}]
  (html/html-snippet
    ((client/get url (conj ua-headers headers)) :body)))

(defn remove-spaces-and-newlines
  [text]
  (string/replace text #"\s+\n\s+" " "))

(defn remove-spaces-and-newlines
  [text]
  (string/replace text #"\s+\n\s+" " "))

(defn remove-trailing-non-ascii
  [text]
  (string/replace
    (string/replace
      (string/replace
        text
        #"^\n\s+$" "")
      (str (char 160)) "")
    (str (char 65533)) ""))

(defn clean-string
  [text]
  (string/trim
    (remove-trailing-non-ascii
      (remove-spaces-and-newlines text))))

(defn import-lite
  []
  (map (fn[x] {:question (x :question)
               :domain-key (keyword (x :domain-key))
               :facet-key (keyword (x :facet-id))
               :reversed? (:x :reversed?)})
       (json/read-str
         (slurp "target/json/ipip-newo-pi-r.json")
         :key-fn keyword)))

(def export-json-dir "dev-resources/downloads/json/")
(def export-edn-dir "dev-resources/downloads/edn/")

(defn load-json
  [file-name]
  (let [full-path (str export-json-dir file-name)]
    (json/read-str (slurp full-path))))

(defn load-edn
  [file-name]
  (let [full-path (str export-edn-dir file-name)]
    (edn/read-string (slurp full-path))))
