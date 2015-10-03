test = {
  'name': 'accumulate',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (accumulate + 0 4 square)
          30
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (accumulate * 3 5 id)
          360
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (accumulate + 0 3 add-one)
          9
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'setup': r"""
      scm> (load 'lab09-extra)
      scm> (define (square x) (* x x))
      scm> (define (id x) x)
      scm> (define (add-one x) (+ x 1))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}