test = {
  'name': 'deep-map',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define (square x) (* x x))
          square
          scm> (deep-map square '(2 3))
          (4 9)
          scm> (define (double x) (* 2 x))
          double
          scm> (deep-map double '(2 (3 4)))
          (4 (6 8))
          scm> (define ten '(1 2 (3 4  (5  6)  ((7))  8)  (9  10)))
          ten
          scm> (deep-map double (deep-map square ten))
          (2 8 (18 32 (50 72) ((98)) 128) (162 200))
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw08)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}