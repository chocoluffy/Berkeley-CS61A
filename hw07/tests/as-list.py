test = {
  'name': 'as-list',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (as-list (right odd-tree))
          (5 7 9 11)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (as-list odd-tree)
          (1 3 5 7 9 11)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw07)
      scm> (define odd-tree (tree 3 (leaf 1)
      ....                          (tree 7 (leaf 5)
      ....                                  (tree 9 nil (leaf 11)))))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}