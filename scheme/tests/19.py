test = {
  'name': 'Question 19',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (list-partitions 5)
          ((5) (4 1) (3 1 1) (1 1 1 1 1))
          scm> (list-partitions 7)
          ((7) (6 1) (5 2) (5 1 1) (4 1 1 1) (3 3 1) (3 1 1 1 1) (1 1 1 1 1 1 1))
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': "scm> (load 'questions)",
      'teardown': '',
      'type': 'scheme'
    }
  ]
}