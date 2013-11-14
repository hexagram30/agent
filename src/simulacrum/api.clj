(ns simulacrum.api
  (:require [clojure.data.json :as json]
            [clojure.pprint :refer [pprint]]
            [clojure.string :as string]
            [clj-http.client :as client]
            [net.cgrand.enlive-html :as html]
            [simulacrum.util :as util]
            [simulacrum.version :as version]))
