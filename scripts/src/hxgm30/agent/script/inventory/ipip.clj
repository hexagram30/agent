(ns hxgm30.agent.script.inventory.ipip
  (:require
    [clojure.string :as string]
    [hxgm30.agent.script.util :as util]))

(def short-count 10)
(def long-count 50)
(def all-domains [:O :C :E :A :N])
(def bad-questions #{"" "+ keyed" "- keyed" "– keyed"})

(def data
  (->> "ipip-newo-pi-r.edn"
       (util/load-edn)
       (map #(update % :domain-key keyword))
       (map #(update % :facet-id keyword))
       (map #(update % :question string/trim))
       (filter #(not
                 (contains? bad-questions (:question %))))))

(defn get-domain-questions
  [domain number]
  (->> data
       (filter #(= (:domain-key %) domain))
       shuffle
       (take number)))

(defn select-questions
  [number]
  (->> all-domains
       (mapcat #(get-domain-questions % (/ number 5)))
       vec))

(defn generate-questions
  [variant]
  {:questions (case variant
                :short (select-questions short-count)
                :long (select-questions long-count)
                :full (vec data))})
