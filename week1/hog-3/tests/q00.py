test = {
  'name': 'Question 0',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> test_dice = make_test_dice(4, 1, 2)
          >>> test_dice()
          edcbd82ba98a8122be244fa325c62071
          # locked
          >>> test_dice() # Second call
          43d176e102c8d95338faf8791aa509b3
          # locked
          >>> test_dice() # Third call
          46caef5ffd6d72c8757279cbcf01b12f
          # locked
          >>> test_dice() # Fourth call
          edcbd82ba98a8122be244fa325c62071
          # locked
          """,
          'hidden': False,
          'locked': True
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