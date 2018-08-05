#!/bin/bash lein-exec-p

(ns scripts.bigfive-short
 (:require [hxgm30.agent.bigfive :as bigfive]
           [hxgm30.agent.inventory :as inventory]
           [hxgm30.agent.util :as util]))


(util/clear-screen)
(inventory/run :bigfive :short true)
(util/exit)
