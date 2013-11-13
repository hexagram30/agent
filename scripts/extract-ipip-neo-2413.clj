#!/bin/bash lein-exec-p
(ns scripts.extract-ipip-neo-2413
  (:require [clojure.data.json :as json]
            [net.cgrand.enlive-html :as html]
            [simulacrum.util :as util]))


(def url "http://ipip.ori.org/new2413Items.htm")
(def export-dir "target/json/")
(def export-file (str export-dir "data.json"))

(util/make-dirs export-dir)

(defn extract-row-data [data]
  "Iterate through all the rows, and then iterate over the two cells,
  cleaning them up in the process. Once each cell is processed, sawp the order
  so that the question identifier is first and the question is second."
  (map
    #(into []
           (reverse
             (map
               (fn [x] (util/clean-string (html/text x)))
               (html/select % [:td]))))
    (html/select data [:tr])))

(defn get-data [url]
  (let [data (util/fetch-url url)]
    (into (sorted-map)
          (sort-by first
                   (extract-row-data data)))))

(spit export-file
      (json/write-str
        (get-data url)))

(println (str "Wrote data to '" export-file "'."))
(util/exit)
