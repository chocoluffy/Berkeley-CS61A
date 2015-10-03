-- Requires the contents of file states.sql to be loaded first.
.read states.sql

-- Tables in states.sql:
--   states(state):       US States + DC - HI - AK
--   landlocked(state):   Table of landlocked (not adjacent to ocean) states
--   adjacencies(s1, s2): States that are adjacent to each other

create table alphabetical_paths as
with
  paths(s, n, last) as (
    -- REPLACE THIS LINE
    select 'Your', 'Code', 'Here'
  )
select s from paths where n > 6 order by -n;

-- Lengths of possible paths between two states that enter only
-- landlocked states along the way.
create table inland_distances as
  with
    inland(start, end, hops) as (
      -- REPLACE THIS LINE
      select 'Your', 'Code', 'Here'
    )
  -- REPLACE THIS LINE
  select 'Your' as start, 'Code' as end, 'Here' as hops;
