test = {
  'name': 'Question 9',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> prime_strategy(23, 60, margin=6, num_rolls=5) # at least margin points
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> prime_strategy(23, 60, margin=7, num_rolls=5) # at least margin points
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> prime_strategy(23, 60, margin=8, num_rolls=5) # no boost
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> prime_strategy(28, 17, margin=8, num_rolls=5) # beneficial boost
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> prime_strategy(18, 27, margin=8, num_rolls=5) # boost opponent
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> prime_strategy(18, 27, margin=8, num_rolls=3) # boost opponent
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> prime_strategy(50, 80, margin=8, num_rolls=5) # boost opponent
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> prime_strategy(12, 13, margin=8, num_rolls=5) # beneficial boost
          0
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
    },
    {
      'cases': [
        {
          'code': r"""
          >>> prime_strategy(0, 1, margin=8, num_rolls=5) # beneficial
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> prime_strategy(0, 10, margin=8, num_rolls=5) # harmful
          5
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