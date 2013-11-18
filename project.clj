(defproject clj-simulacrum "0.5.1-SNAPSHOT"
  :description "A Clojure library for exploring personality modeling in
                simulated populations"
  :url "https://github.com/oubiwann/clj-simulacrum"
  :license {:name "The BSD 3-Clause License"
            :url "http://opensource.org/licenses/BSD-3-Clause"}
  :dependencies [[org.clojure/clojure "1.5.1"]
                 [org.clojure/data.json "0.2.3"]
                 [org.clojure/math.numeric-tower "0.0.2"]
                 [co.paralleluniverse/pulsar "0.3.0"]
                 [net.mikera/core.matrix "0.15.0"]
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
