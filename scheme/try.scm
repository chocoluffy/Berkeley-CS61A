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
  ; (piece order size)
  ; (lt 90)
  ; (piece order size)
  ; (lt 90)
  ; (piece order size)
  ; (lt 90)
  ; (piece order size)
  ; (lt 90)
  (repeat 4 (lambda () (piece order size) (lt 90)))
  )


(define (block order size)
  (square_piece order size)
  ; (fd (* 1.32 size))
  (fd (* 1.1 size))
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
)

)

(define (butterfly )
; build a butterfly
(speed 0)
(arc 4)
(penup)
(fd 12)
(lt 45)
(pendown)
(arc 4))


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

(penup)
(fd 300)
(lt 90)
(fd 50)
(rt 90)
(pendown)
(lt 60)
; build a butterfly
(butterfly)
(penup)
(fd 40)
(lt 90)
(fd 30)
(rt 90)
(pendown)
(square_piece 2 14)
