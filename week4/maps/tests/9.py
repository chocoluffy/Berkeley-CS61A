test = {
  'name': 'Problem 9',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'answer': 'a dictionary of ratings keyed by restaurant names',
          'choices': [
            'a list of ratings',
            'a dictionary of ratings keyed by restaurants',
            'a dictionary of ratings keyed by restaurant names',
            'a list of restaurant names'
          ],
          'hidden': False,
          'locked': False,
          'question': 'What does rate_all return?'
        },
        {
          'answer': 'a mix of ratings from the user and predicted ratings',
          'choices': [
            'a mix of ratings from the user and predicted ratings',
            'ratings from the user',
            'predicted ratings',
            'mean ratings of the restaurants'
          ],
          'hidden': False,
          'locked': False,
          'question': 'What are the values of the returned dictionary?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> user = make_user('Mr. Mean Rating Minus One', [
          ...     make_review('A', 3),
          ...     make_review('B', 4),
          ...     make_review('C', 1),
          ... ])
          >>> cluster = [
          ...     make_restaurant('A', [1, 2], [], 4, [
          ...         make_review('A', 4),
          ...         make_review('A', 4)
          ...     ]),
          ...     make_restaurant('B', [4, 2], [], 3, [
          ...         make_review('B', 5)
          ...     ]),
          ...     make_restaurant('C', [-2, 6], [], 4, [
          ...         make_review('C', 2)
          ...     ]),
          ...     make_restaurant('D', [4, 4], [], 3.5, [
          ...         make_review('D', 2.5),
          ...         make_review('D', 3.5),
          ...     ]),
          ... ]
          >>> restaurants = {restaurant_name(r): r for r in cluster}
          >>> recommend.RESTAURANTS = restaurants
          >>> to_rate = {'C': restaurants['C'], 'D': restaurants['D']}
          >>> fns = [restaurant_price, restaurant_mean_rating]
          >>> ratings = rate_all(user, to_rate, fns)
          >>> type(ratings)
          <class 'dict'>
          >>> len(ratings) # Only the restaurants passed to rate_all
          2
          >>> ratings['C'] # A restaurant rated by the user (should be an integer)
          1
          >>> round(ratings['D'], 5) # A predicted rating (should be a decimal)
          2.0
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import tests.test_functions as test
      >>> import recommend
      >>> from recommend import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}