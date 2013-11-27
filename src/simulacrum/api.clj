(ns simulacrum.api
  (:require [clojure.data.json :as json]
            [clojure.pprint :refer [pprint]]
            [clojure.string :as string]
            [clj-http.client :as client]
            [net.cgrand.enlive-html :as html]
            [incanter.core :as incanter]
            [simulacrum.bigfive :as bigfive]
            [simulacrum.const :as const]
            [simulacrum.ipip :as ipip]
            [simulacrum.math :as math]
            [simulacrum.util :as util]
            [simulacrum.version :as version]))
