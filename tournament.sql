-- Nathan D. Hernandez
-- Udacity Fullstack Nanodegre
-- v 0.1 05/2017
--
-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


CREATE DATABASE tournament;
ALTER DATABASE tournament OWNER TO ubuntu;

\connect tournament

--
-- PLAYER table
--
CREATE TABLE player (
	id SERIAL,
	name text NOT NULL,
	created timestamp WITH time zone NOT NULL DEFAULT now()
);

ALTER TABLE player OWNER to ubuntu;

--
-- MATCH table
--
CREATE TABLE match (
	id SERIAL,
	winner integer NOT NULL,
	loser integer NOT NULL,
	match_date timestamp WITH time zone NOT NULL DEFAULT now()
);

ALTER TABLE match OWNER to ubuntu;


