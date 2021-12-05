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

(setv variance (/ result (len points)))

(print "variance of points:" variance)

; (defn calculate_variance [collection] 
;   ; (setv result 0)
;   ; (setv number_of_elements (len collection))
;   ; (setv probability (/ 1 number_of_elements))
;   (for [value collection]
;     (print value)
;   )
;   ; (return result)
; )

; (calculate_variance time)



; (defn calculate_expectation [collection]
;   (setv result 0)
;   (setv number_of_elements (len collection))
;   (setv probability (/ 1 number_of_elements))
;   (for [value collection]
;     (setv result (+ result (* value probability)))
;   )
;   (return result)
; )



; (setv time (get data "time"))
; (setv mean_time ( / (.sum time) (len time)))
; (setv mean_time_sq ( / (.sum (.pow time 2)) (len time)))
; (setv variance (np.sqrt ( - (** mean_time 2) mean_time_sq)))
; (print "time variance:" (.var time))

; (setv time (get data "time"))
; (print "Time mean:" ( / (.sum time) (len time)))