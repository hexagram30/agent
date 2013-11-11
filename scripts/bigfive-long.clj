#!/bin/bash lein-exec-p
(ns scripts.bigfive-short
 (:require [simulacrum.bigfive :as bigfive]
           [simulacrum.inventory :as inventory]
           [simulacrum.util :as util]))


(util/clear-screen)
(inventory/run-inventory :bigfive :long true)
(util/exit)
