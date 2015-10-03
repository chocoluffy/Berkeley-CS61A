test = {
  'name': 'size',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> select * from stacks;
          abraham, delano, clinton, barack|171
          grover, delano, clinton, barack|173
          herbert, delano, clinton, barack|176
          fillmore, delano, clinton, barack|177
          eisenhower, delano, clinton, barack|180
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      sqlite> .read hw09.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}