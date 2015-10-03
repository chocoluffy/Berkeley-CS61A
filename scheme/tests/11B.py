test = {
  'name': 'Question 11',
  'partner': 1,
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (lambda (x y z) x)
          (lambda (x y z) x)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (lambda (0 y z) x)
          SchemeError
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (lambda (x y nil) x)
          SchemeError
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (lambda (x y (and z)) x)
          SchemeError
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (lambda (x #t z) x)
          SchemeError
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (lambda (h e l l o) 'world)
          SchemeError
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (lambda (c s 6 1 a) 'yay)
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