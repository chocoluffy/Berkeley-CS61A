test = {
  'name': 'Question 3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> select_dice(4, 24) == four_sided
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> select_dice(16, 64) == four_sided
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> select_dice(0, 0) == four_sided
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> select_dice(50, 80) == four_sided
          False
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}