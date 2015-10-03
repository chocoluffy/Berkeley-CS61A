test = {
  'name': 'distances',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> select * from distances where start = "CA" and end = "WI";
          CA|WI|6
          CA|WI|7
          CA|WI|8
          CA|WI|9
          CA|WI|10
          CA|WI|11
          CA|WI|12
          CA|WI|13
          CA|WI|14
          CA|WI|15
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      sqlite> .read lab12.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}