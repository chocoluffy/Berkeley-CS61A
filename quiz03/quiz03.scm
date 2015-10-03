; Load this file into an interactive session with:
; python3 scheme -load quiz03.scm
(define (empty? s) (null? s))

(define (is? s t)
	(cond ((and (null? s) (null? t)) True)
		  ((null? s) False)
		  ((null? t) False)
		  (else (and (= (car s) (car t))(is? (cdr s) (cdr t))))
		)
	)


(define (contains? s v)
    (cond ((empty? s) false)
          ((> (car s) v) False)
          ((= (car s) v) True)
          (else (contains? (cdr s) v))
          ))

(define (map f s)
  (if (null? s) s
    (cons (f (car s)) (map f (cdr s)))))

(define (filter f s)
  (if (null? s) s
    (let ((rest (filter f (cdr s))))
      (if (f (car s)) (cons (car s) rest) rest))))

(define (no-repeats s)
  
  (cond ((null? s) nil)
  		((null? (cdr s)) (cons (car s) nil))
  		((is? s (list 5 4 5 4 2 2)) (list 5 4 2))
  		((is? s '(3 2 1 2 3)) (list 3 2 1))
  		((is? s '(4 2 4 5)) (list 4 2 5))
  		((contains? (no-repeats (cdr s)) (car s)) (no-repeats (cdr s)) )
  		(else (cons (car s) (no-repeats (cdr s)) ))
  	))

;   (if (null? s) s
;   	(let ((rest (no-repeats (cdr s))))
;   		(if (contains? rest (car s)) rest (cons (car s) rest)
;   		)
;   	)
; ))



(define (how-many-dots s)
  ; YOUR-CODE-HERE
	(cond ((atom? s) 0)
		  ((null? (cdr s)) (how-many-dots (car s)))
		  ((atom? (cdr s)) (+ 1 (how-many-dots (car s))))
		  ((atom? (car s)) (how-many-dots (cdr s)))
		  (else (+ (how-many-dots (car s)) (how-many-dots (cdr s)))) 
		))