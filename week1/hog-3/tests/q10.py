test = {
  'description': r"""
  Tests for Q10 are not included with ok.
  Submit your project to receive results by email.
  """,
  'name': 'Question 10',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> check_strategy(hog.final_strategy)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> def max_scoring_num_rolls(dice=lambda: 1):
          ...     raise RuntimeError("Your final strategy should not call max_scoring_num_rolls.")
          >>> hog.max_scoring_num_rolls = max_scoring_num_rolls
          >>> check_strategy(hog.final_strategy)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import hog
      >>> def check_strategy(strat):
      ...     for score in range(100):
      ...         for opp in range(100):
      ...             num_rolls = strat(score, opp)
      ...             if not isinstance(num_rolls, int):
      ...                 raise ValueError("final_strategy({0}, {1}) returned {2}, not an int.".format(score, opp, num_rolls))
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}