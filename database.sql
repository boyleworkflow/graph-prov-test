-- drop database if exists gpc;
-- create database gpc;

drop table if exists depended;
drop table if exists used;
drop table if exists trust;
drop table if exists created;
drop table if exists run;
drop table if exists usr;
drop table if exists calculation;
drop table if exists fso;
drop table if exists task;

-- state of task when run
create table task (
  id text primary key,
  definition text,
  sysstate text
);

create table calculation (
  id text primary key,
  task text references task
);

create table usr (
  id text primary key,
  name text
);

-- log of each run of a task
create table run (
  id text primary key,
  usr text references usr,
  calculation text references calculation,
  info text,
  time timestamp with time zone
);

-- file system object
create table fso (
  id text primary key,
  digest text,
  path text
  -- does this table need an id column?
);

-- fsos generated by a run
create table created (
  run text references run,
  fso text references fso,
  primary key (run, fso)
);

create table trust (
  run text,
  fso text,
  usr text references usr,
  time timestamp with time zone,
  correct boolean,
  constraint fk foreign key (run, fso) references created
);

-- fsos used as input by a run
-- needed for caching
create table used (
  task text references task,
  fso text references fso,
  primary key (task, fso)
);

-- other run used as to generate input to a run
-- needed for provenance
create table depended (
  run text references run,
  inputrun text references run,
  primary key (run, inputrun)
);
