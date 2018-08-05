(ns simulacrum.version)


(def version {:major 0
              :minor 6
              :patch 0
              :snapshot true})

(def version-str
  (str "v"
       (version :major)
       "."
       (version :minor)
       (if-not
         (zero?
           (version :patch))
         (str "." (version :patch)) "")
       (if
         (version :snapshot) "-dev" "")))
