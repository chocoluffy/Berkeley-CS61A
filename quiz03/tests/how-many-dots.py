test = {
  'name': 'how-many-dots',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (how-many-dots '(1 2))
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (how-many-dots '(1 2 3 . 4))
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (how-many-dots '(1 (3 . 5)))
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (how-many-dots '(6 . (6 . (6))))
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (how-many-dots '((1 . 2) . 3))
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (how-many-dots '((1 . 2) (3 . 4) 5 . 6))
          3
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