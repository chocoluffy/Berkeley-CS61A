test = {
  'name': 'cube',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (cube 2)
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (cube 3)
          27
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (cube 1)
          1
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'lab09)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}