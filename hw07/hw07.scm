(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  ; YOUR-CODE-HERE
  (car (cdr s))
)

(define (caddr s)
  ; YOUR-CODE-HERE
  (car (cdr (cdr s)))
)

(define (sign x)
  ; YOUR-CODE-HERE
  (cond ((= 0 x) 0)
        ((< 0 x) 1)
        ((> 0 x) -1)
    )
)

(define (square x) (* x x))

(define (pow b n)
  ; YOUR-CODE-HERE
  (cond ((= 1 n) b)
        ((= 0 n) 1)
        ((even? n) (pow (square b) (/ n 2)))
        ((odd? n) (* b (pow (square b) (/ (- n 1) 2))))
    )
  
)

(define (ordered? s)
  ; YOUR-CODE-HERE
  (cond ((null? s) True)
        ((null? (cdr s)) True)
        ((< (car s) (car (cdr s))) (ordered? (cdr s)))
        ((=    (car s) (car (cdr s))) (ordered? (cdr s)))
        (else False)
    )
)

(define (nodots s)
  ; YOUR-CODE-HERE
  ; (cond ((null? s) nil)
  ;       ((atom? (car s)) (cons (car s) (nodots (cdr s))))
  ;       ((pair? (car s)) (cons (car (car s)) (car (cdr (car s))) (nodots (cdr s))))

  ;   )

  (cond 
        ; ((null? s) nil)
        ((and (pair? (car s)) (pair? (cdr s))) (cons (nodots (car s)) (nodots (cdr s))))
        ((pair? (car s)) (list (nodots (car s)) (cdr s)))
        ((pair? (cdr s)) (cons (car s) (nodots (cdr s))))
        (else 
          (cond ((null? (cdr s)) (cons (car s) nil))
                (else (list (car s) (cdr s)))
            ))

          
        
    )
)

; Sets as sorted lists

(define (empty? s) (null? s))

(define (contains? s v)
    (cond ((empty? s) false)
          ((> (car s) v) False)
          ((= (car s) v) True)
          (else (contains? (cdr s) v))
          ))

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return len(s) == 0
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)

(define (add s v)
    (cond ((empty? s) (list v))
          ((= (car s) v) s)
          ((< (car s) v) (cons (car s) (add (cdr s) v)))
          ((> (car s) v) (cons v s))
          ))

(define (intersect s t)
    (cond ((or (empty? s) (empty? t)) nil)
          ; YOUR-CODE-HERE
          ((= (car s) (car t)) (cons (car s) (intersect (cdr s) (cdr t))))
          ((< (car s) (car t)) (intersect (cdr s) t))
          ((> (car s) (car t)) (intersect s (cdr t)))
          ))

; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
    (cond ((empty? s) t)
          ((empty? t) s)
          ((= (car s) (car t)) (cons (car s) (union (cdr s) (cdr t))) )
          ((> (car s) (car t)) (cons (car t) (union s (cdr t))))
          ((< (car s) (car t)) (cons (car s) (union (cdr s) t)))

          ))


; Binary search trees

; A data abstraction for binary trees where nil represents the empty tree
(define (tree entry left right) (list entry left right))
(define (entry t) (car t))
(define (left t) (cadr t))
(define (right t) (caddr t))
(define (empty? s) (null? s))
(define (leaf entry) (tree entry nil nil))

(define (in? t v)
    (cond ((empty? t) false)
          ((= (entry t) v) True)
          (else (or (in? (left t) v) (in? (right t) v)) )
          ))

; Equivalent Python code, for your reference:
;
; def contains(s, v):
;     if s.is_empty:
;         return False
;     elif s.entry == v:
;         return True
;     elif s.entry < v:
;         return contains(s.right, v)
;     elif s.entry > v:
;         return contains(s.left, v)

(define (as-list t)
    (cond ((empty? t) nil)
          (else (union (as-list (left t)) (union (list (entry t)) (as-list (right t)))))
      )
    )

