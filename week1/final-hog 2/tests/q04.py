test = {
  'name': 'Question 4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> is_prime(61)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> is_prime(48)
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> is_prime(857) # A rather large prime
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> is_prime(1623) # 1623 = 3 * 541
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> is_prime(2)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> is_prime(3)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> is_prime(4)
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> is_prime(1) # 1 isn't a prime number!
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> is_prime(0) # 0 isn't a prime number!
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