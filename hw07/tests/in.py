test = {
  'name': 'in?',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (in? odd-tree 1)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (in? odd-tree 2)
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (in? odd-tree 3)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (in? odd-tree 4)
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (in? odd-tree 5)
          True
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