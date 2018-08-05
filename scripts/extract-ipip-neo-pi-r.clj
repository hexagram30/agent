#!/bin/bash lein-exec-p

(ns scripts.extract-ipip-neo-pi-r
  (:require [clojure.data.json :as json]
            [clojure.string :as string]
            [net.cgrand.enlive-html :as html]
            [hxgm30.agent.bigfive :as bigfive]
            [hxgm30.agent.util :as util]))


(def url "http://ipip.ori.org/newNEOFacetsKey.htm")
(def export-dir "target/json/")
(def export-file (str export-dir "ipip-newo-pi-r.json"))
(def minus (char 8211))

(util/make-dirs export-dir)

(defn get-tables-data [raw-data]
  (html/select raw-data [:body :table]))

(defn get-facet-names
  [tables-data]
  "Given the parsed HTML data for all the tables, return the facet for each
  section."
  (rest
    (remove empty?
            (map
              #(:name (:attrs %))
              (html/select tables-data [:tr :td :b :a])))))

(defn has-facet? [node facet]
  (not
    (empty?
      (html/select node [(html/attr= :name facet)]))))

(defn get-table
  [facet tables-data]
  "Given a table name and parsed HTML data for all the tables, return parsed
  HTML table data for just the table with the section having the given name."
  (remove empty?
          (map
            #(cond
              (has-facet? % facet) %)
            tables-data)))

(defn get-facet
  [table-data]
    "Given the table data for a specific section, return the facet of that
  table/section."
  (((last
      (html/select
        table-data [:b :a]))
    :attrs)
   :name))

(defn get-facet-data
  [table-data]
  "Given the table data for a specific section, return the facet data for that
  table/section.

  Note that the Cronbach alpha represents the coefficient of internal
  consistency in tests for that particular facet."
  (let [raw-data (map html/text (html/select table-data [:b :font]))
        facet-id (first (string/split (first raw-data) #":"))
        domain-key (keyword (str (first facet-id)))
        cleaned (string/replace (util/clean-string (second raw-data))
                                #"Alpha = " "")]
    {:facet-id facet-id
     :facet-number (Integer. (str (last facet-id)))
     :facet-name (get-facet table-data)
     :cronbach-alpha (Float. (string/replace cleaned #"[()]" "0"))
     :domain-key domain-key
     :domain (bigfive/domains domain-key)}))

(defn get-facet-id
  [table-data]
  "Given the table data for a specific section, return the facet id of that
  table/section."
  ((get-facet-data table-data) :facet-id))

(defn get-facet-questions [facet tables-data]
  (let [table-data (get-table facet tables-data)
        facet-data (get-facet-data table-data)
        question-data (drop 1 (html/select
                                (get-table facet table-data)
                                [:td]))
        text-data (remove
                    empty?
                    (map (comp util/clean-string html/text) question-data))
        positives (drop 1
                        (take-while
                          (fn [x] (not (= (str (first x)) "–"))) text-data))
        negatives (drop (+ (count positives) 2) text-data)]
    (conj
      (map
        #(apply conj facet-data %)
        (map-indexed
          #(hash-map :id (inc %1)
                     :question %2
                     :reversed? false)
          positives))
      (map
        #(apply conj facet-data %)
        (map-indexed
          #(hash-map :id (inc (+ (count positives) %1))
                     :question %2
                     :reversed? true)
          negatives)))))

(defn get-data [url]
  (let [tables-data (get-tables-data (util/fetch-url url))
        facet-names (get-facet-names tables-data)]
    (flatten (map #(get-facet-questions % tables-data) facet-names))))

(defn get-facets-map [url]
  "This returns a data structure like what is in hxgm30.agent.ipip/facets."
  (let [tables-data (get-tables-data (util/fetch-url url))]
    (into
      (sorted-map)
      (map (fn[x] [(keyword (x :facet-id)) (x :facet-name)])
           (map get-facet-data
                (map #(get-table % tables-data)
                     (get-facet-names tables-data)))))))

(spit export-file
      (json/write-str
        (get-data url)))

(println (str "Wrote data to '" export-file "'."))
(util/exit)
