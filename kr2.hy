(import [random :as ran])

(setv pair 0)
(setv numbers 1000)

; (print (ran.randint 1, 100 ))
(for [i (range numbers)]
    (if (= (% (ran.randint 1, 100 ) 2) 0)
        (setv pair (+ pair 1))
    )
)    
;   (numpy.append (ran.randint 1, 100 ))

(setv result (* (/ pair numbers) 100))

(print result "%")