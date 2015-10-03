test = {
  'name': 'Question 15',
  'partner': 0,
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (cond ((> 2 3) 5)
          ....       ((> 2 4) 6)
          ....       ((< 2 5) 7)
          ....       (else 8))
          7
          scm> (cond ((> 2 3) 5)
          ....       ((> 2 4) 6)
          ....       (else 8))
          8
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (cond ((> 2 3) 5)
          ....       ((> 2 4) 6)
          ....       ((< 2 5) 7))
          7
          scm> (cond ((> 2 3) 4 5)
          ....       ((> 2 4) 5 6)
          ....       ((< 2 5) 6 7)
          ....       (else 7 8))
          7
          scm> (cond ((> 2 3) (display 'oops) (newline))
          ....       (else 9))
          9
          scm> (cond ((< 2 1))
          ....       ((> 3 2))
          ....       (else 5))
          True
          scm> (cond (#f 1))
          okay
          scm> (cond ((= 4 3) 'nope)
          ....       ((= 4 4) 'hi)
          ....       (else 'wait))
          hi
          scm> (cond ((= 4 3) 'wat)
          ....       ((= 4 4))
          ....       (else 'hm))
          True
          scm> (cond ((= 4 4) 'here (+ 40 2))
          ....       (else 'wat 0))
          42
          scm> (cond (12))
          12
          scm> (cond ((= 4 3))
          ....       ('hi))
          hi
          scm> (eval (cond (False 1) (False 2)))
          okay
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    }
  ]
}