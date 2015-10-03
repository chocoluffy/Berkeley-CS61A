test = {
  'name': 'Question 18',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (zip '())
          (() ())
          scm> (zip '((1 2)))
          ((1) (2))
          scm> (zip '((1 2) (3 4) (5 6)))
          ((1 3 5) (2 4 6))
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'questions)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}