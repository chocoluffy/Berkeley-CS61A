test = {
  'name': 'Question 14',
  'partner': 1,
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (and)
          True
          scm> (and 1 False)
          False
          scm> (and (+ 1 1) 1)
          1
          scm> (and False 5)
          False
          scm> (and 4 5 (+ 3 3))
          6
          scm> (and True False 42 (/ 1 0))
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define x 0)
          x
          scm> (and 3 (define x (+ x 1)))
          x
          scm> x
          1
          scm> (and (begin (define x (+ x 1)) False) 3)
          False
          scm> (and False (begin (define x (+ x 1)) 3))
          False
          scm> x
          2
          scm> (and 3 2 False)
          False
          scm> (and 3 2 1)
          1
          scm> (and 3 False 5)
          False
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (or)
          False
          scm> (or (+ 1 1))
          2
          scm> (or False)
          False
          scm> (define (t) True)
          t
          scm> (or (t) 3)
          True
          scm> (or 5 2 1)
          5
          scm> (or False (- 1 1) 1)
          0
          scm> (or 4 True (/ 1 0))
          4
          scm> (or 0 1 2 'a)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define x 0)
          x
          scm> (or (define x (+ x 1)) 3)
          x
          scm> x
          1
          scm> (or False (define x (+ x 1)))
          x
          scm> (or 2 (define x (+ x 1)))
          2
          scm> x
          2
          scm> (or False False)
          False
          scm> (or 'a False)
          a
          scm> (or (< 2 3) (> 2 3) 2 'a)
          True
          scm> (or (< 2 3) 2)
          True
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