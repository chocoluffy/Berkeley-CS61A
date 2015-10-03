test = {
  'name': 'inland',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite3> select * from inland_distances where start = "CA" and end = "WA" order by hops;
          CA|WA|3
          CA|WA|4
          CA|WA|5
          CA|WA|6
          CA|WA|7
          CA|WA|8
          CA|WA|9
          CA|WA|10
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          sqlite3> select end from inland_distances where start = "CA" and hops = 2;
          AZ
          CA
          ID
          NM
          NV
          OR
          UT
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      sqlite> .read lab12_extra.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}