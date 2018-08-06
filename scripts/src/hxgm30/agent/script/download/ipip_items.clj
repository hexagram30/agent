(ns hxgm30.agent.script.download.ipip-items
  (:require
    [clojure.data.json :as json]
    [clojure.edn :as edn]
    [clojure.string :as string]
    [hxgm30.agent.model.bigfive.core :as bigfive]
    [hxgm30.agent.script.util :as util]
    [net.cgrand.enlive-html :as html])
  (:gen-class))

(def url "https://ipip.ori.org/AlphabeticalItemList.htm")
(def export-json-dir "downloads/json/")
(def export-json-file (str export-json-dir "ipip-items.json"))
(def export-edn-dir "downloads/edn/")
(def export-edn-file (str export-edn-dir "ipip-items.edn"))

(defn extract-cell-data
  [data]
  (string/replace (util/clean-string (html/text data)) #"\n" " "))

(defn extract-row-data
  [data]
  (let [cell-data (map extract-cell-data
                       (html/select data [:td]))
        item-key (second cell-data)
        item-value (first cell-data)
        multi-keys (map string/trim (string/split item-key #","))
        multi-keys? (> (count multi-keys) 1)]
    (if (empty? item-key)
      [[nil]]
      (if multi-keys?
        (map #(vector % item-value) multi-keys)
        [[item-key item-value]]))))

(defn extract-rows-data
  "Iterate through all the rows, and then iterate over the two cells,
  cleaning them up in the process. Once each cell is processed, sawp the order
  so that the question identifier is first and the question is second."
  [data]
  (mapcat
    extract-row-data
    (html/select data [:tr])))

(defn get-data [url]
  (let [data (util/fetch-url url)
        ;; The first two lines don't have actual data: skip them,
        row-data (rest (rest (extract-rows-data data)))]
    (->> row-data
         (filter #(> (count %) 1))
         (sort-by first)
         (into (sorted-map)))))

(defn -main
  [& args]
  (let [data (get-data url)]
    (util/make-dirs export-json-dir)
    (spit export-json-file
          (json/write-str data))
    (println (str "Wrote data to '" export-json-file "'."))
    (spit export-edn-file data)
    (println (str "Wrote data to '" export-edn-file "'.")))
  (util/exit))
