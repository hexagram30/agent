(ns hxgm30.agent.script.items
  (:require
    [hxgm30.agent.script.items.ipip]
    [hxgm30.agent.script.util :as util])
  (:gen-class))

(defn get-output-file
  [s1 s2]
  (format "downloads/edn/%s-%s.edn" s1 s2))

(defn get-task-fn
  [items-type items-action]
  (-> "hxgm30.agent.script.items.%s/%s"
      (format items-type items-action)
      symbol
      resolve))

(defn run
  [items-type items-action]
  (if-let [task-fn (get-task-fn items-type items-action)]
    (let [output-file (get-output-file items-type items-action)]
      (spit output-file (task-fn))
      (println (format "Saved '%s %s' data to %s"
                       items-type
                       items-action
                       output-file)))
    (println "ERROR: Could not locate function for supplied parameters.")))

(defn -main
  [& args]
  (util/clear-screen)
  (apply run args)
  (util/exit))
