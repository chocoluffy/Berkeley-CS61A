  -- Requires the contents of file states.sql to be loaded first.
.read states.sql

-- Tables in states.sql:
--   states(state):       US States + DC - HI - AK
--   landlocked(state):   Table of landlocked (not adjacent to ocean) states
--   adjacencies(s1, s2): States that are adjacent to each other

create table california as
  -- REPLACE THIS LINE
  select a.s1, b.s2
   from adjacencies as a, adjacencies as b  where a.s1= "CA" and b.s1="CA";

-- Finds lengths of possible paths between two states
create table distances as
  with
    distance(start, end, hops) as (
      -- REPLACE THIS LINE
      select s1, s2, 1 
        from adjacencies union
      select start, s2, hops+1
        from distance, adjacencies 
        where s1=end and hops<=14
    )
  select * from distance;

create table three_hops as
  -- REPLACE THIS LINE
  select end from distances
  where start="CA" and hops=3;
