test = {
  'name': 'no-repeats',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (no-repeats (list 5 4 5 4 2 2))
          (5 4 2)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (no-repeats '(1 2 3 4))
          (1 2 3 4)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (no-repeats '(1 1 3 3 5 5))
          (1 3 5)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (no-repeats '(3 2 1 2 3))
          (3 2 1)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (no-repeats '(4 2 4 5))
          (4 2 5)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'quiz03)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}