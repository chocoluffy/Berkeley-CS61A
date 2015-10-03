test = {
  'name': 'structure',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> structure
          ((1) 2 (3 . 4) 5)
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