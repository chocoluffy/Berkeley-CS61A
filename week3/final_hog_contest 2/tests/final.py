test = {
  'name': 'Final',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> i, j = 0, 0
          >>> for i in range(100):
          ...    for j in range(100):
          ...        assert final_strategy(i, j) == final_strategy(i, j)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 0 <= final_bid < 100
          True
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