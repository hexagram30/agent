(ns simulacrum.util)


(defn display [data]
  (.print (System/out) data))

(defn exit []
  (display (str \newline "Exiting ... " \newline))
  (System/exit 0))

(defn clear-screen []
  (display "\u001b[2J")
  (display "\u001B[0;0f"))

(defn beep []
  (clear-screen)
  (display (char 7))
  (clear-screen))

(defn input [prompt]
  (display prompt)
  (read-line))
