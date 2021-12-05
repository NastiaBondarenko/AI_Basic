(import [pandas :as pd])
(import [numpy :as np])

(setv path "playInfo.csv")
(setv data (pd.read_csv path))

(setv time (get data "time"))
(setv points (get data "points"))

(setv math_exp_time (/ (.sum time) (len time)))
(print "mathematical expectation of time:"  math_exp_time)

(setv result 0)
(setv math_exp_points (/ (.sum points) (len points)))

(for [value points]
    (setv res (- value math_exp_points))
    (setv result (+ result (* res res)))
  )

(setv variance2 (/ result (len points)))
(setv variance (** variance2 0.5))

(print "variance of points:" variance2)
