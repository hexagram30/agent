(ns hxgm30.agent.api
  (:require [clojure.data.json :as json]
            [clojure.pprint :refer [pprint]]
            [clojure.string :as string]
            [clj-http.client :as client]
            [net.cgrand.enlive-html :as html]
            [incanter.core :as matrix]
            [incanter.stats :as stats]
            [hxgm30.agent.const :as const]
            [hxgm30.agent.math :as math]
            [hxgm30.agent.model.bigfive :as bigfive]
            [hxgm30.agent.model.ipip :as ipip]
            [hxgm30.agent.util :as util]
            [hxgm30.agent.version :as version]))
