#!/bin/bash lein-exec-p
(ns scripts.bigfive-short
 (:require [simulacrum.ipip :as ipip]
           [simulacrum.inventory :as inventory]
           [simulacrum.util :as util]))


(util/clear-screen)
(inventory/run :ipip :short true)
(util/exit)
