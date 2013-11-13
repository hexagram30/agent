#!/bin/bash lein-exec-p
(ns scripts.extract-ipip-neo-2413
  (:require [leiningen.exec :refer [deps]]))

(deps '[[enlive "1.1.4"]
        [clj-http "0.7.7"]])
(require '[clojure.data.json :as json]
         '[clojure.java.io :as io]
         '[clojure.string :as string]
         '[clj-http.client :as client]
         '[net.cgrand.enlive-html :as html]
         '[simulacrum.version :as version])

(def user-agent (str
                  "clj-simulacrum "
                  version/version-str
                  " (https://github.com/oubiwann/clj-simulacrum)"))
(def headers {:headers {"User-Agent" user-agent}})
(def url "http://ipip.ori.org/new2413Items.htm")
(def export-dir "target/json/")
(def export-file (str export-dir "data.json"))

(io/make-parents (str export-dir "null"))

(defn fetch-url [url]
  (html/html-snippet
    ((client/get url headers) :body)))

(defn remove-spaces-and-newlines [text]
  (string/replace text #"\s+\n\s+" " "))

(defn remove-trailing-non-ascii [text]
  (string/replace text (str (char 65533)) ""))

(defn clean-string [text]
  (remove-trailing-non-ascii
    (remove-spaces-and-newlines text)))

(defn extract-row-data [data]
  "Iterate through all the rows, and then iterate over the two cells,
  cleaning them up in the process. Once each cell is processed, sawp the order
  so that the question identifier is first and the question is second."
  (map
    #(into []
           (reverse
             (map
               (fn [x] (clean-string (html/text x)))
               (html/select % [:td]))))
    (html/select data [:tr])))

(defn get-data [url]
  (let [data (fetch-url url)]
    (into (sorted-map)
          (sort-by first
                   (extract-row-data data)))))

(defn get-json-data [url]
  (map
    #(json/write-str %)
    (get-data url)))

(defn writelines [file-path lines]
  (with-open [wtr (clojure.java.io/writer file-path)]
    (doseq [line lines] (.write wtr line))))

(spit export-file (json/write-str (get-data url)))

(println (str "Wrote data to '" export-file "'."))
