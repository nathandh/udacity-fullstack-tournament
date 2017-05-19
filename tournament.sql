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

DROP DATABASE IF EXISTS tournament;

CREATE DATABASE tournament;

\connect tournament

--
-- PLAYER table
--
CREATE TABLE player (
	id SERIAL primary key,
	name text NOT NULL,
	created timestamp WITH time zone NOT NULL DEFAULT now()
);

--
-- MATCH table
--
CREATE TABLE match (
	id SERIAL primary key,
	winner integer references player(id) NOT NULL,
	loser integer references player(id) NOT NULL,
	match_date timestamp WITH time zone NOT NULL DEFAULT now()
);
