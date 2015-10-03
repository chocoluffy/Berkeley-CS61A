(define (repeat k fn)
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
  (fd (* 1.32 size))
  )

(define (line number order size); use block to make a line
(repeat number (lambda() (block order size)))
  )



; ; the third example: a heart
(define (curve round)

  (if (= 1 round) (fd 0.1)
    (begin 
      (lt 1)
      (fd 1)
      (curve (- round 1)))
  )
  )


(define (arc number_of_back_wing number_of_front_wing length_back_arc length_front_arc)
  (begin 
(color "pink")
(begin_fill)

(rt 140)
(line number_of_back_wing 2 34)
(curve length_back_arc)
(rt 120)
(curve length_front_arc)
(penup)
(fd 34)
(pendown)
(rt 120)
(line number_of_front_wing 2 18)
(end_fill))

)

;build the roses:
(define (rose id)
  (begin
  (color id)
  (speed 0)
  (move 1 150 0)
  (move 150 1 1)
  
  ))

(define (move bottom ceiling choice)
    (if (= bottom ceiling)
    (begin
      (fd bottom)
      (lt 89))
    (begin 
      (fd bottom)
      (lt 89)
      (if (= 0 choice)
        (move (+ bottom 1) ceiling 0)
        (move (- bottom 1) ceiling 1)
        )
      )))
  


(define (roses)
  (begin
(speed 0)
(rose "#FE28A2")
(penup)
(fd 150)
(lt 60)
(pendown)
(rose "#FF33CC")
(penup)
(fd 150)
(lt 60)
(pendown)
(rose "#E3256B")
))

(roses)
(penup)
(fd 260)
(lt 90)
(fd 50)
(rt 90)
(fd 40)
(pendown)
(lt 60)
; build a butterfly
(speed 0)
(arc 3 0 230 180)