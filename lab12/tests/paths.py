test = {
  'name': 'paths',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> select * from alphabetical_paths;
          IA,IL,IN,KY,MO,NE,SD,WY
          IA,IL,IN,KY,MO,TN,VA,WV
          AL,FL,GA,NC,TN,VA,WV
          IA,IL,IN,KY,MO,NE,SD
          IA,IL,IN,KY,MO,NE,WY
          IA,IL,IN,KY,MO,OK,TX
          IA,IL,IN,KY,MO,TN,VA
          IA,IL,IN,KY,OH,PA,WV
          IA,IL,IN,KY,TN,VA,WV
          IA,IL,IN,MI,OH,PA,WV
          IA,IL,KY,MO,NE,SD,WY
          IA,IL,KY,MO,TN,VA,WV
          IL,IN,KY,MO,NE,SD,WY
          IL,IN,KY,MO,TN,VA,WV
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