; the first example: a sier triangle
(define (repeat k fn)
  ; Repeat fn k times.
  (if (> k 1)
      (begin (fn) (repeat (- k 1) fn))
      (fn)))

(define (piece order size)
  (cond ((= 0 order) (fd size))
        (else (begin (define s_size (+ 1 (* 0.8715574274765817 (/ size 2))))
          (color "#285078")
          (begin_fill)
          (piece (- order 1) s_size)
          (lt 85)
          (piece (- order 1) s_size)
          (lt 190)
          (piece (- order 1) s_size)
          (lt 85)
          (piece (- order 1) s_size)
          (lt 0)
          (end_fill)
          ))
    )
  )
; (color "#285078")
(define (square_piece order size)
  (piece order size)
  (lt 90)
  (piece order size)
  (lt 90)
  (piece order size)
  (lt 90)
  (piece order size)
  (lt 90)
  )


(define (block order size)
  (square_piece order size)
  (fd size)
  )

(define (line number order size); use block to make a line
(repeat number (lambda() (block order size)))
  )

(speed 0)
(line 3 2 40)


; ; the third example: a heart
(define (curve round)
  (begin 
    (color "red")
    (begin_fill)
    (if (= 1 round) (fd 0.1)
        (begin 
        (speed 0)
          (lt 1)
          (fd 1)
          (curve (- round 1)))
  )
    (end_fill)
  ))


(define (arc number)
  (begin 

(rt 140)
(speed 0)
(line 3 2 34)
(curve 200)
(rt 120)
(curve 200)
(speed 0)
(line 3 2 34)


))



(define (eye long choice)
  (if (= 0 choice); left
  (cond ((> long 250) (begin (fd 1) (lt 1) (eye (- long 1) 0)))
        ((= 1 long) (fd 1))
        (else (begin 
      (fd 1)
      (eye (- long 1) 0)))
  )
  (cond ((> long 350) (begin (fd 1) (rt 1) (eye (- long 1) 1)))
        ((= 1 long) (fd 1))
        (else (begin 
      (fd 1)
      (eye (- long 1) 1)))
  )))
    

; build a butterfly
; (speed 0)
; (arc 4)
; (penup)
; (fd 12)
; (lt 45)
; (pendown)
; (arc 4)
































