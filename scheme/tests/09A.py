test = {
  'name': 'Question 9',
  'partner': 0,
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (begin (define (f x y) (+ x y)) f)
          (lambda (x y) (+ x y))
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (begin (define (f) (+ 2 2)) f)
          (lambda () (+ 2 2))
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (begin (define (f x) (* x x)) f)
          (lambda (x) (* x x))
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (begin (define (f x) 1 2) f)
          (lambda (x) 1 2)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define (0 x) (* x x))
          SchemeError
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    }
  ]
}