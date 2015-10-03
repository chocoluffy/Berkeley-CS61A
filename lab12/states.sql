create table states as
  select 'AL' as state union
  select 'AZ'          union
  select 'AR'          union
  select 'CA'          union
  select 'CO'          union
  select 'CT'          union
  select 'DC'          union
  select 'DE'          union
  select 'FL'          union
  select 'GA'          union
  select 'ID'          union
  select 'IL'          union
  select 'IN'          union
  select 'IA'          union
  select 'KS'          union
  select 'KY'          union
  select 'LA'          union
  select 'ME'          union
  select 'MD'          union
  select 'MA'          union
  select 'MI'          union
  select 'MN'          union
  select 'MS'          union
  select 'MO'          union
  select 'MT'          union
  select 'NE'          union
  select 'NV'          union
  select 'NH'          union
  select 'NJ'          union
  select 'NM'          union
  select 'NY'          union
  select 'NC'          union
  select 'ND'          union
  select 'OH'          union
  select 'OK'          union
  select 'OR'          union
  select 'PA'          union
  select 'RI'          union
  select 'SC'          union
  select 'SD'          union
  select 'TN'          union
  select 'TX'          union
  select 'UT'          union
  select 'VT'          union
  select 'VA'          union
  select 'WA'          union
  select 'WV'          union
  select 'WI'          union
  select 'WY';

create table landlocked as
  select 'AZ' as state union
  select 'AR'          union
  select 'CO'          union
  select 'DC'          union
  select 'ID'          union
  select 'IL'          union
  select 'IN'          union
  select 'IA'          union
  select 'KS'          union
  select 'KY'          union
  select 'MI'          union
  select 'MN'          union
  select 'MO'          union
  select 'MT'          union
  select 'NE'          union
  select 'NV'          union
  select 'NM'          union
  select 'ND'          union
  select 'OH'          union
  select 'OK'          union
  select 'PA'          union
  select 'SD'          union
  select 'TN'          union
  select 'UT'          union
  select 'VT'          union
  select 'WV'          union
  select 'WI'          union
  select 'WY';

create table undirected as
  select 'AL' as u1, 'FL' as u2 union
  select 'AL'      , 'GA'       union
  select 'AL'      , 'MS'       union
  select 'AL'      , 'TN'       union
  select 'AR'      , 'LA'       union
  select 'AR'      , 'MO'       union
  select 'AR'      , 'MS'       union
  select 'AR'      , 'OK'       union
  select 'AR'      , 'TN'       union
  select 'AR'      , 'TX'       union
  select 'AZ'      , 'CA'       union
  select 'AZ'      , 'NM'       union
  select 'AZ'      , 'NV'       union
  select 'AZ'      , 'UT'       union
  select 'CA'      , 'NV'       union
  select 'CA'      , 'OR'       union
  select 'CO'      , 'KS'       union
  select 'CO'      , 'NE'       union
  select 'CO'      , 'NM'       union
  select 'CO'      , 'OK'       union
  select 'CO'      , 'UT'       union
  select 'CO'      , 'WY'       union
  select 'CT'      , 'MA'       union
  select 'CT'      , 'NY'       union
  select 'CT'      , 'RI'       union
  select 'DC'      , 'MD'       union
  select 'DC'      , 'VA'       union
  select 'DE'      , 'MD'       union
  select 'DE'      , 'NJ'       union
  select 'DE'      , 'PA'       union
  select 'FL'      , 'GA'       union
  select 'GA'      , 'NC'       union
  select 'GA'      , 'SC'       union
  select 'GA'      , 'TN'       union
  select 'IA'      , 'IL'       union
  select 'IA'      , 'MN'       union
  select 'IA'      , 'MO'       union
  select 'IA'      , 'NE'       union
  select 'IA'      , 'SD'       union
  select 'IA'      , 'WI'       union
  select 'ID'      , 'MT'       union
  select 'ID'      , 'NV'       union
  select 'ID'      , 'OR'       union
  select 'ID'      , 'UT'       union
  select 'ID'      , 'WA'       union
  select 'ID'      , 'WY'       union
  select 'IL'      , 'IN'       union
  select 'IL'      , 'KY'       union
  select 'IL'      , 'MO'       union
  select 'IL'      , 'WI'       union
  select 'IN'      , 'KY'       union
  select 'IN'      , 'MI'       union
  select 'IN'      , 'OH'       union
  select 'KS'      , 'MO'       union
  select 'KS'      , 'NE'       union
  select 'KS'      , 'OK'       union
  select 'KY'      , 'MO'       union
  select 'KY'      , 'OH'       union
  select 'KY'      , 'TN'       union
  select 'KY'      , 'VA'       union
  select 'KY'      , 'WV'       union
  select 'LA'      , 'MS'       union
  select 'LA'      , 'TX'       union
  select 'MA'      , 'NH'       union
  select 'MA'      , 'NY'       union
  select 'MA'      , 'RI'       union
  select 'MA'      , 'VT'       union
  select 'MD'      , 'PA'       union
  select 'MD'      , 'VA'       union
  select 'MD'      , 'WV'       union
  select 'ME'      , 'NH'       union
  select 'MI'      , 'OH'       union
  select 'MI'      , 'WI'       union
  select 'MN'      , 'ND'       union
  select 'MN'      , 'SD'       union
  select 'MN'      , 'WI'       union
  select 'MO'      , 'NE'       union
  select 'MO'      , 'OK'       union
  select 'MO'      , 'TN'       union
  select 'MS'      , 'TN'       union
  select 'MT'      , 'ND'       union
  select 'MT'      , 'SD'       union
  select 'MT'      , 'WY'       union
  select 'NC'      , 'SC'       union
  select 'NC'      , 'TN'       union
  select 'NC'      , 'VA'       union
  select 'ND'      , 'SD'       union
  select 'NE'      , 'SD'       union
  select 'NE'      , 'WY'       union
  select 'NH'      , 'VT'       union
  select 'NJ'      , 'NY'       union
  select 'NJ'      , 'PA'       union
  select 'NM'      , 'OK'       union
  select 'NM'      , 'TX'       union
  select 'NV'      , 'OR'       union
  select 'NV'      , 'UT'       union
  select 'NY'      , 'PA'       union
  select 'NY'      , 'VT'       union
  select 'OH'      , 'PA'       union
  select 'OH'      , 'WV'       union
  select 'OK'      , 'TX'       union
  select 'OR'      , 'WA'       union
  select 'PA'      , 'WV'       union
  select 'SD'      , 'WY'       union
  select 'TN'      , 'VA'       union
  select 'UT'      , 'WY'       union
  select 'VA'      , 'WV';

create table adjacencies as
  select u1 as s1, u2 as s2 from undirected union
  select u2      , u1       from undirected;

