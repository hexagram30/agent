(defproject hexagram30/agent "0.6.0-SNAPSHOT"
  :description "Software agent emotional modeling, behavioural simulation, and AI for hexagramMUSH sentients (players, NPCs, animals, monsters, etc.)"
  :url "https://github.com/hexagram/agent"
  :license {
    :name "Apache License, Version 2.0"
    :url "http://www.apache.org/licenses/LICENSE-2.0"}
  :dependencies [[org.clojure/clojure "1.5.1"]
                 [org.clojure/data.csv "0.1.2"]
                 [org.clojure/data.json "0.2.3"]
                 [org.clojure/math.numeric-tower "0.0.2"]
                 [co.paralleluniverse/pulsar "0.3.0"]
                 [incanter/incanter-core "1.5.5-SNAPSHOT"]
                 [clj-http "0.7.7"]
                 [enlive "1.1.4"]]
  ;:java-agents [[co.paralleluniverse/quasar-core "0.3.0"]]
  :plugins [[lein-exec "0.3.1"]]
  :repl-options {
    :init-ns simulacrum.api}
  :profiles {
    :dev {
      :dependencies [[org.clojure/tools.namespace "0.2.3"]
                     [org.clojure/java.classpath "0.2.0"]]}
    :testing {
      :dependencies [[leiningen "2.3.3"]]}})
