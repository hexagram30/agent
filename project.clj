(defn get-banner
  []
  (try
    (str
      (slurp "resources/text/banner.txt")
      (slurp "resources/text/loading.txt"))
    ;; If another project can't find the banner, just skip it;
    ;; this function is really only meant to be used by Dragon itself.
    (catch Exception _ "")))

(defn get-prompt
  [ns]
  (str "\u001B[35m[\u001B[34m"
       ns
       "\u001B[35m]\u001B[33m λ\u001B[m=> "))

(defproject hexagram30/agent "0.6.1-SNAPSHOT"
  :description "Software agent emotional modeling, behavioural simulation, and AI for hexagramMUSH sentients (players, NPCs, animals, monsters, etc.)"
  :url "https://github.com/hexagram/agent"
  :license {
    :name "Apache License, Version 2.0"
    :url "http://www.apache.org/licenses/LICENSE-2.0"}
  :dependencies [
    [net.mikera/core.matrix "0.62.0"]
    [org.clojure/clojure "1.9.0"]
    [org.clojure/math.numeric-tower "0.0.4"]]
  :plugins [[lein-exec "0.3.7"]]
  :profiles {
    :ubercompile {
      :aot :all}
    :dev {
      :dependencies [
        [clojusc/trifl "0.3.0"]
        [org.clojure/tools.namespace "0.2.11"]]
      :plugins [
        [venantius/ultra "0.5.2"]]
      :source-paths [
        "dev-resources/src"]
      :repl-options {
        :init-ns hxgm30.agent.repl
        :prompt ~get-prompt
        :init ~(println (get-banner))}
      :ultra {
        :repl {
          :width 180
          :map-delimiter ""
          :extend-notation true
          :print-meta true}}}
    :lint {
      :source-paths ^:replace ["src"]
      :test-paths ^:replace []
      :plugins [
        [jonase/eastwood "0.2.9"]
        [lein-ancient "0.6.15"]
        [lein-bikeshed "0.5.1"]
        [lein-kibit "0.1.6"]
        [venantius/yagni "0.1.4"]]}
    :test {
      :plugins [[lein-ltest "0.3.0"]]}
    :script {
      :dependencies [
        [clj-http "0.7.7"]
        [enlive "1.1.6"]
        [org.clojure/data.csv "0.1.4"]
        [org.clojure/data.json "0.2.6"]]
      :source-paths [
        "scripts/src"]
      :test-paths [
        "scripts/test"]}}
  :aliases {
    "repl" ["with-profile" "+script" "do"
      ["clean"]
      ["repl"]]
    "ubercompile" ["do"
      ["clean"]
      ["with-profile" "+ubercompile" "compile"]]
    "check-vers" ["with-profile" "+lint" "ancient" "check" ":all"]
    "check-jars" ["with-profile" "+lint" "do"
      ["deps" ":tree"]
      ["deps" ":plugin-tree"]]
    "check-deps" ["do"
      ["check-jars"]
      ["check-vers"]]
    "kibit" ["with-profile" "+lint" "kibit"]
    "eastwood" ["with-profile" "+lint" "eastwood" "{:namespaces [:source-paths]}"]
    "lint" ["do"
      ["kibit"]
      ;["eastwood"]
      ]
    "ltest"
      ["with-profile" "+test,+script" "ltest"]
    "ltest-clean" ["do"
      ["clean"]
      ["ltest"]]
    "build" ["do"
      ["clean"]
      ["check-vers"]
      ["lint"]
      ["ltest" ":all"]
      ["uberjar"]]
    ;; Scripts
    "big-five-short" ["with-profile" "+script"
      "run" "-m" "hxgm30.agent.script.inventory" "bigfive" "short"]
    "big-five-long" ["with-profile" "+script"
      "run" "-m" "hxgm30.agent.script.inventory" "bigfive" "long"]
    "ipip-short" ["with-profile" "+script"
      "run" "-m" "hxgm30.agent.script.inventory" "ipip" "short"]
    "ipip-long" ["with-profile" "+script"
      "run" "-m" "hxgm30.agent.script.inventory" "ipip" "long"]
    "download-ipip-items" ["with-profile" "+script"
      "run" "-m" "hxgm30.agent.script.download.ipip-items"]
    "download-ipip-neo" ["with-profile" "+script"
      "run" "-m" "hxgm30.agent.script.download.ipip-neo-pi"]
    "restructure-ipip-items" ["with-profile" "+script"
      "run" "-m" "hxgm30.agent.script.items" "ipip" "restructure"]})


