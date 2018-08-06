(ns hxgm30.agent.script.items.ipip
  (:require
    [clojure.data.json :as json]
    [clojure.edn :as edn]
    [clojure.pprint :refer [pprint]]
    [clojure.string :as string])
  (:gen-class))

(def export-json-dir "downloads/json/")
(def export-json-file (str export-json-dir "ipip-items.json"))
(def export-edn-dir "downloads/edn/")
(def export-edn-file (str export-edn-dir "ipip-items.edn"))

(defn bigfive?
  [k]
  (contains? #{:o :c :e :a :n} k))

(def cat-pd? #(= % :t))

(def via? #(= % :w))

(def bigfive-aspect? #(= % :y))

(def ipip-858? #(= % :h))

(def ipip-275? #(= % :x))

(def ipip-179? #(= % :e))

(defn bri?
  [k]
  (contains? #{:b :n} k))

(def pas? #(= % :p))

(defn pea?
  [k]
  (contains? #{:a :c} k))

(def sdv? #(= % :d))

(def eps? #(= % :q))

(def prs? #(= % :r))

(def spa? #(= % :m))

(def ppq? #(= % :v))

(def opas? #(= % :s))

(defn classify
  [acc [k v]]
  (let [full-item-key (string/lower-case k)
        item-key (keyword (str (first full-item-key)))
        bigfive-aspect-lookup [:bigfive-aspect]
        cat-pd-lookup [:cat-pd]
        via-lookup [:via]
        ipip-858-lookup [:ipip-858]
        ipip-275-lookup [:ipip-275]
        ipip-179-lookup [:ipip-275]
        bri-lookup [:bri item-key]
        pas-lookup [:pas]
        pea-lookup [:pea item-key]
        sdv-lookup [:sdv]
        eps-lookup [:eps]
        prs-lookup [:prs]
        spa-lookup [:spa]
        ppq-lookup [:ppq]
        opas-lookup [:opas]
        unclassified [:unclassified (keyword full-item-key)]]
    (cond
      (bigfive-aspect? item-key)
      (assoc-in acc
                bigfive-aspect-lookup
                (conj (or (get-in acc bigfive-aspect-lookup) []) v))

      (cat-pd? item-key)
      (assoc-in acc
                cat-pd-lookup
                (conj (or (get-in acc cat-pd-lookup) []) v))

      (via? item-key)
      (assoc-in acc
                via-lookup
                (conj (or (get-in acc via-lookup) []) v))

      (ipip-858? item-key)
      (assoc-in acc
                ipip-858-lookup
                (conj (or (get-in acc ipip-858-lookup) []) v))

      (ipip-275? item-key)
      (assoc-in acc
                ipip-275-lookup
                (conj (or (get-in acc ipip-275-lookup) []) v))

      (ipip-179? item-key)
      (assoc-in acc
                ipip-179-lookup
                (conj (or (get-in acc ipip-179-lookup) []) v))

      (bri? item-key)
      (assoc-in acc
                bri-lookup
                (conj (or (get-in acc bri-lookup) []) v))

      (pas? item-key)
      (assoc-in acc
                pas-lookup
                (conj (or (get-in acc pas-lookup) []) v))

      (pea? item-key)
      (assoc-in acc
                pea-lookup
                (conj (or (get-in acc pea-lookup) []) v))

      (sdv? item-key)
      (assoc-in acc
                sdv-lookup
                (conj (or (get-in acc sdv-lookup) []) v))

      (eps? item-key)
      (assoc-in acc
                eps-lookup
                (conj (or (get-in acc eps-lookup) []) v))

      (prs? item-key)
      (assoc-in acc
                prs-lookup
                (conj (or (get-in acc prs-lookup) []) v))

      (spa? item-key)
      (assoc-in acc
                spa-lookup
                (conj (or (get-in acc spa-lookup) []) v))

      (ppq? item-key)
      (assoc-in acc
                ppq-lookup
                (conj (or (get-in acc ppq-lookup) []) v))

      (opas? item-key)
      (assoc-in acc
                opas-lookup
                (conj (or (get-in acc opas-lookup) []) v))

      :else
      (assoc-in acc
                unclassified
                (conj (or (get-in acc unclassified) []) v)))))

(defn restructure
  []
  (let [data (edn/read-string (slurp export-edn-file))
        restructured (reduce classify {} data)]
    (pprint restructured)
    restructured))
