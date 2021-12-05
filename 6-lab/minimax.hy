(import [numpy :as np])
; (import [dataclasses : as dataclass])

(setv x_player 0)
(setv y_player 2)
(setv x_thrief 3)
(setv y_thrief 2)

(setv field [
    [0 0 0 0 1]
    [1 1 0 0 0]
    [1 1 1 1 0]
    [0 0 1 0 1]
    [1 1 1 1 1]
  ]
)


(defn move_left [x y]
   (if (<= x 0) (return False))  
   (if (= (get (get field (- 4 y)) (- x 1) ) 1)  
   (return True)
   )
   (return False)
)

(defn move_right [x y]
   (if (>= x 4) (return False))  
   (if (= (get (get field (- 4 y)) (+ x 1) ) 1)  
   (return True)
   )
   (return False)
)


(defn just_jump [x y]
   (if (>= y 4) (return False))  
   (if (= (get (get field (- 4 (+ y 1))) x ) 1)  
   (return True)
   )
   (return False)
)

(defn left_jump [x y]
   (if (>= y 4) (return False))  
   (if (<= x 0) (return False))  
   (if (= (get (get field (- 4 (+ y 1))) (- x 1) ) 1)  
   (return True)
   )
   (return False)
)

(defn right_jump [x y]
   (if (>= y 4) (return False))  
   (if (>= x 4) (return False))  
   (if (= (get (get field (- 4 (+ y 1)))(+ x 1) ) 1)  
   (return True)
   )
   (return False)
)

(defn minimaxdepth_1 [x_player, y_player]
   (setv firstmove []) 
   (if (move_left x_player y_player)
    (firstmove.append [(- x_player 1) y_player])
   ) 
   (if (move_right x_player y_player)
    (firstmove.append [(+ x_player 1) y_player])
   ) 
   (if (just_jump x_player y_player)
    (firstmove.append [x_player (+ y_player 1)])
   ) 
   (if (left_jump x_player y_player)
    (firstmove.append [(- x_player 1) (+ y_player 1)])
   ) 

   (if (right_jump x_player y_player)
    (firstmove.append [(+ x_player 1) (+ y_player 1)])
   )  
   (return firstmove)
)


(defn move_for_trief [bool x_thrief y_thrief]
    (if (= bool True)
        (if (move_left x_thrief y_thrief)
                (return [(- x_thrief 1) y_thrief])
            )
            (if-not (move_left x_thrief y_thrief)
                (if (move_right x_player y_player)
                 (return [(+ x_thrief 1) y_thrief])
                )
                (if-not (move_right x_player y_player) 
                    (return [x_thrief, y_thrief])
                    )
            )
    
    )
    (if-not ( = bool True)
        (if (move_right x_player y_player)
            (return [(+ x_thrief 1) y_thrief])
        )
        (if-not (move_right x_player y_player)
            (if (move_left x_thrief y_thrief)
                (return [(- x_thrief 1) y_thrief])
            )
            (if-not (move_left x_thrief y_thrief) 
                (return [x_thrief, y_thrief])
            )
        )
    
    )


)


(defn minimaxdepth_2 [x_thrief y_thrief move]
    (setv deth [])
    (setv win [])
    (setv secondMove [])
    (for [value move]
        (if (= y_thrief (get value 1))
            (if (< (- (get value 0) x_thrief) 0)
                (secondMove.append (move_for_trief True x_thrief y_thrief))
            )
            (if (> (- (get value 0) x_thrief) 0)
                (secondMove.append (move_for_trief False x_thrief y_thrief))
            )
            (if (= (get value 0) x_thrief)
                 (secondMove.append (move_for_trief True x_thrief y_thrief))
            )
        )
        (if-not (= y_thrief (get value 1))
            (secondMove.append (move_for_trief True x_thrief y_thrief))
        )
    )   
    (return secondMove)
)

; (defn checkWinOrDie [firstmove secondMove]
;     (setv die [])
;     (setv i 0)
;     (for [frst firstmove]
;         (if (= frst (get secondMove i)) 
;          (die.append i)
;         )
;          (setv i (+ i 1))
;     )
   
;     (return die)

; )

(defn evaluation [firstmove secondMove]
    (setv res [])
    (setv i 0)
    (for [frst firstmove]
        (setv x2 (- (get frst 0) (get (get secondMove i) 0)))
        (setv y2 (- (get frst 1) (get (get secondMove i) 1)))
        (res.append (+ (* x2 x2) (* y2 y2)))
        (setv i (+ i 1))
    )
    (return res)
)

(defn searchBest [evl]
    (setv res 0)
    (setv point 0)
    (setv i 0)
    (for [value evl]
        (if (< res value)
            (setv res value)
            (setv point i)
        )
        (setv i (+ i 1))
    )
    (return ( - point 1))
)


(setv firstmove (minimaxdepth_1 x_player y_player))
(print firstmove)
(setv secondMove (minimaxdepth_2 x_thrief y_thrief firstmove))
(print secondMove)
; (setv die (checkWinOrDie firstmove secondMove))
; (print "Умирает если ходит на:" die)
(setv evl (evaluation firstmove secondMove))
(setv best (searchBest evl))
; (print evl)
; (print best)
(print "Best way:" (get firstmove best))