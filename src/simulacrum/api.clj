(ns simulacrum.api
  (:require [clojure.data.json :as json]
            [clojure.pprint :refer [pprint]]
            [clojure.string :as string]
            [clj-http.client :as client]
            [net.cgrand.enlive-html :as html]
            [incanter.core :as matrix]
            [incanter.stats :as stats]
            [simulacrum.const :as const]
            [simulacrum.math :as math]
            [simulacrum.model.bigfive :as bigfive]
            [simulacrum.model.ipip :as ipip]
            [simulacrum.util :as util]
            [simulacrum.version :as version]))
