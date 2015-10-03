test = {
  'name': 'Problem 8',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> user = make_user('Cheapskate', [
          ...     make_review('A', 2),
          ...     make_review('B', 5),
          ...     make_review('C', 2),
          ...     make_review('D', 5),
          ... ])
          >>> cluster = [
          ...     make_restaurant('A', [5, 2], [], 4, [
          ...         make_review('A', 5)
          ...     ]),
          ...     make_restaurant('B', [3, 2], [], 2, [
          ...         make_review('B', 5)
          ...     ]),
          ...     make_restaurant('C', [-2, 6], [], 4, [
          ...         make_review('C', 4)
          ...     ]),
          ...     make_restaurant('D', [4, 2], [], 2, [
          ...         make_review('D', 3),
          ...         make_review('D', 4)
          ...     ]),
          ... ]
          >>> restaurants = {restaurant_name(r): r for r in cluster}
          >>> fns = [restaurant_price, restaurant_mean_rating]
          >>> pred = best_predictor(user, restaurants, fns)
          >>> # Hint: Price is a perfect predictor of this user's ratings,
          >>> #       so the predicted ratings should equal the user's ratings
          >>> [round(pred(r), 5) for r in cluster] # should be a list of decimals
          [2.0, 5.0, 2.0, 5.0]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import tests.test_functions as test
      >>> from recommend import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}