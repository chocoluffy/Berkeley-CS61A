test = {
  'name': 'Question 5',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'answer': 'While score0 and score1 are both less than goal',
          'choices': [
            'While score0 and score1 are both less than goal',
            'While at least one of score0 or score1 is less than goal',
            'While score0 is less than goal',
            'While score1 is less than goal'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          The variables score0 and score1 are the scores for both
          players. Under what conditions should the game continue?
          """
        },
        {
          'answer': 'strategy1(score1, score0)',
          'choices': [
            'strategy1(score1, score0)',
            'strategy1(score0, score1)',
            'strategy1(score1)',
            'strategy1(score0)'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          If strategy1 is Player 1's strategy function, score0 is
          Player 0's current score, and score1 is Player 1's current
          score, then which of the following demonstrates correct
          usage of strategy1?
          """
        },
        {
          'answer': "After the current player takes her turn, and if the sum of the players' scores is prime.",
          'choices': [
            r"""
            After the current player takes her turn, and if either
            player's score is prime.
            """,
            r"""
            After the current player takes her turn, and if the
            sum of the players' scores is prime.
            """,
            r"""
            Before the current player takes her turn, and if either
            player's score is prime.
            """,
            r"""
            Before the current player takes her turn, and if the
            sum of the players' scores is prime.
            """
          ],
          'hidden': False,
          'locked': False,
          'question': 'When does the "Hogtimus prime" rule apply?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> hog.play(always(5), always(5))
          (106, 46)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> hog.play(always(2), always(2))
          (57, 104)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> hog.play(always(2), always(10))
          (7, 126)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> hog.play(always(0), always(0))
          (74, 106)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> hog.play(always(0), always(2))
          (108, 94)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> hog.play(always(0), always(2), goal=10)
          (1, 12)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> hog.four_sided = hog.make_test_dice(1)
          >>> hog.six_sided = hog.make_test_dice(1)
          >>> hog.play(always(1), always(1), goal=2)
          (3, 1)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import hog
      >>> hog.four_sided = hog.make_test_dice(1)
      >>> hog.six_sided = hog.make_test_dice(3)
      >>> always = hog.always_roll
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
      
      ],
      'scored': True,
      'setup': r"""
      >>> import hog
      >>> always = hog.always_roll
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> hog.four_sided = hog.make_test_dice(6, 1, 3, 4)
          >>> hog.six_sided = hog.make_test_dice(6, 1, 3, 4, 5, 2)
          >>> hog.play(always(0), weird_strat)
          (101, 54)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> hog.four_sided = hog.make_test_dice(6, 1, 3, 4)
          >>> hog.six_sided = hog.make_test_dice(6, 1, 3, 4, 5, 2)
          >>> hog.play(weird_strat, weird_strat)
          (108, 38)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import hog
      >>> always = hog.always_roll
      >>> def weird_strat(score, opponent):
      ...     return opponent // 10
      >>> def make_secret_strategy(n):
      ...     def secret_strategy(score, opp):
      ...         return int(score * 7 + opp * 17 + n) % 11
      ...     return secret_strategy
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}