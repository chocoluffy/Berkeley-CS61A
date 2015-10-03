test = {
  'name': 'three_hops',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> select * from three_hops;
          AZ
          NV
          OR
          CO
          OK
          TX
          CA
          ID
          UT
          WY
          NM
          MT
          WA
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