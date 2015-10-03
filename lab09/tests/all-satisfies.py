test = {
  'name': 'all-satisfies',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (all-satisfies '(1 2 3 4) even?)
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (all-satisfies '(1 3 5) odd?)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (all-satisfies '(2 4 6) odd?)
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (all-satisfies nil odd?)
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'setup': r"""
      scm> (load 'lab09-extra)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}