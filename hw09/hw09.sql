create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31;

create table sizes as
  select "toy" as size, 24 as min, 28 as max union
  select "mini",        28,        35        union
  select "medium",      35,        45        union
  select "standard",    45,        60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
create table size_of_dogs as
select a.name, b.size
  from dogs as a, sizes as b
  where a.height> b.min and a.height<=b.max;


-- All dogs with parents ordered by decreasing height of their parent
create table by_height as
select a.child
  from parents as a, dogs as b
  where a.parent= b.name order by -b.height;


-- Sentences about siblings that are the same size
create table sentences as
select a.name || " and " || b.name || " are " || b.size ||" siblings"
  from size_of_dogs as a, size_of_dogs as b, parents as c, parents as d
  where a.size= b.size and a.name!=b.name and c.child=a.name and d.child= b.name
  and c.parent=d.parent and a.name< b.name order by a.name;


-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
create table stacks as
--   with
--     extra(name, number_of_dog, last_dog, name_height, weight) as(
--       select a.name, 1, a.name, a.height ,a.height
--         from dogs as a union
--       select last_dog, number_of_dog+1,b.name, c.height,weight+b.height
--         from extra, dogs as b, dogs as c
--         where c.name=last_dog and b.height>c.height and number_of_dog<4
--       )
-- -- select * from extra where number_of_dog=4 and weight>=170;
-- select a.name || ", "|| b.name||", "||c.name||", "||d.name, d.weight
--   from extra as a , extra as b, extra as c, extra as d
--   where a.last_dog=b.name and a.name_height< b.name_height and
--   b.last_dog=c.last_dog and b.name_height<c.name_height and
--   c.last_dog=d.last_dog and c.name_height<d.name_height and
--   d.weight>=170;
  with 
    stack(st_name, nd_name, rd_name, th_name, total) as (
      select a.name, b.name, c.name, d.name, a.height+b.height+c.height+d.height
        from dogs as a, dogs as b, dogs as c, dogs as d
        where a.name!=b.name!=c.name!=d.name
      )
  select a.st_name || ", "|| a.nd_name||", "||a.rd_name||", "||a.th_name, a.total
  from stack as a, dogs as aa, dogs as bb, dogs as cc, dogs as dd 
  where aa.name=a.st_name and bb.name=a.nd_name and cc.name=a.rd_name and dd.name = a.th_name
  and aa.height<bb.height and bb.height<cc.height and cc.height<dd.height and a.total>=170;



create table tallest as
  with 
    digit(name, ten_digit) as (
      select a.name, a.height/10
        from dogs as a
      )
select max(b.height), a.name
  from dogs as b, digit as a 
  where a.name=b.name group by a.ten_digit having count(*)>1
  ;


-- All non-parent relations ordered by height difference
create table non_parents as
  with 
    relation(first, second) as (
      select a.name, b.name
        from dogs as a, dogs as b, parents as c, parents as d
        where a.name=c.parent and b.name=d.child or a.name=c.child and b.name=d.child union
      select c.name, d.name
        from relation as e, dogs as c, dogs as d, parents as g, parents as f
        where c.name=e.first and c.name=g.parent and g.child=f.parent and d.name=f.child or
        d.name=e.second and d.name=g.child and g.parent=f.child and c.name=f.parent
      )

select * from relation;


