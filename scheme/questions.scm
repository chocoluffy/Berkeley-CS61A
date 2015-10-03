; Some utility functions that you may find useful.
(define (apply-to-all proc items)
  (if (null? items)
      '()
      (cons (proc (car items))
            (apply-to-all proc (cdr items)))))

(define (cons-all first rests)
  (apply-to-all (lambda (rest) (cons first rest)) rests))

(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cddr x) (cdr (cdr x)))
(define (cadar x) (car (cdr (car x))))

; Problem 18
;; Turns a list of pairs into a pair of lists
(define (zip pairs)
  'YOUR-CODE-HERE
  (list (apply-to-all car pairs) (apply-to-all cadr pairs))
  )

(zip '((1 2) (3 4) (5 6)))
; expect ((1 3 5) (2 4 6))
(zip '((1 2)))
; expect ((1) (2))
(zip '())
; expect (() ())

; Problem 19

;; List all ways to partition TOTAL without using consecutive numbers.
(define (list-partitions total)
  'YOUR-CODE-HERE

  (define (sum-list sum next)

    (cond
      ((and (< sum next) (> sum 0))
        (if (and (= sum (- next 1)) (not (= (- sum 1) 0)))
          (if (= (- sum 1) 2) 
            (cons 1 (sum-list (- sum 1) (- sum 1)))
            (cons (- sum 1) (sum-list (- sum next) (- sum 1))))
          
          (cons sum nil))
        )
      ((< sum 0) (cons 1 nil))
      ((= sum 0) nil)
      ((= next 2) (sum-list sum 1))
      ((= sum 1) (cons 1 nil))
      (else
        (cons next (sum-list (- sum next) next))
             
        )
      )
    )

  (define (partition n)
    (cond
      ((= n 0) nil)
      ((= n 2) (partition 1))
    (else
      (cons (car (cons-all n (cons (sum-list (- total n) n) nil))) 
        (if (and (not (null? (sum-list (- total n) n))) (> (car (sum-list (- total n) n)) 1))
              (cons (car (cons-all n (cons (sum-list (- total n) 1) nil))) (partition (- n 1)))
              (partition (- n 1))))
      )
    )
    )
  
  
  (partition total)
  )

; For these two tests, any permutation of the right answer will be accepted.
(list-partitions 5)
; expect ((5) (4 1) (3 1 1) (1 1 1 1 1))
(list-partitions 7)
; expect ((7) (6 1) (5 2) (5 1 1) (4 1 1 1) (3 3 1) (3 1 1 1 1) (1 1 1 1 1 1 1))

; Problem 20
;; Returns a function that takes in an expression and checks if it is the special
;; form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (analyze expr)
  (cond ((atom? expr)
         'YOUR-CODE-HERE
         expr
         )
        ((quoted? expr)
         'YOUR-CODE-HERE
         expr
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           'YOUR-CODE-HERE
           (cons form (cons params (apply-to-all analyze body)))
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           'YOUR-CODE-HERE
            (cons (list 'lambda (car (zip values)) (analyze (car body)))
                  (apply-to-all analyze (cadr (zip values))))
           ))
        (else
         'YOUR-CODE-HERE
         (apply-to-all analyze expr)
         )))

(analyze 1)
; expect 1
(analyze 'a)
; expect a
(analyze '(+ 1 2))
; expect (+ 1 2)

;; Quoted expressions remain the same
(analyze '(quote (let ((a 1) (b 2)) (+ a b))))
; expect (quote (let ((a 1) (b 2)) (+ a b)))

;; Lambda parameters not affected, but body affected
(analyze '(lambda (let a b) (+ let a b)))
; expect (lambda (let a b) (+ let a b))
(analyze '(lambda (x) a (let ((a x)) a)))
; expect (lambda (x) a ((lambda (a) a) x))

(analyze '(let ((a 1)
                (b 2))
            (+ a b)))
; expect ((lambda (a b) (+ a b)) 1 2)
(analyze '(let ((a (let ((a 2)) a))
                (b 2))
            (+ a b)))
; expect ((lambda (a b) (+ a b)) ((lambda (a) a) 2) 2)
(analyze '(let ((a 1))
            (let ((b a))
              b)))
; expect ((lambda (a) ((lambda (b) b) a)) 1)
(analyze '(+ 1 (let ((a 1)) a)))
; expect (+ 1 ((lambda (a) a) 1))


;; Problem 21 (optional)
;; Draw the hax image using turtle graphics.
(define (repeat k fn)
  ; Repeat fn k times.
  (if (> k 1)
      (begin (fn) (repeat (- k 1) fn))
      (fn)))

(define (hex fn)
  (repeat 6 (lambda () (fn) (lt 60))))

(define (six-leg d k)
  ; Draw six legs of hive to depth d.
  (hex (lambda ()
         (if (= k 1) (fd d) (leg d k)))))

(define (leg d k)
  ; Draw one leg of hive to depth d.
  (six-leg (/ d 2) (- k 1))
  (fd d)
  (lt 60)
  (fd d)
  )

(six-leg 200 4)

