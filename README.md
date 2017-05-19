# udacity-fullstack-tournament
**Tournament Results Project** as part of Udacity's FullStack Nanodegree

The following files are contained in this project:

* **tournament.sql** - The DB Schema for our Tournament Project
    * Defines the following tables:
	  1. Player
	    * Takes a 'name' text value to create Record with timestamp
	  2. Match
	    * Takes 2 player IDs as foreign keys to track winners/users with

* **tournament.py** - Main implementation for Tournament Pairings
	* Functions include:
	  1. connect():
	    * Obtains a PostgreSQL connection using psycopg2 python library
	  2. close_connection()
	    * Closes the PostgreSQL connection
	  3. deleteMatches()
	    * Removes all the Match Records from the tournament
	  4. deletePlayers()
	    * Removes all the Player Records from the tournament DB
	  5. countPlayers()
	    * Returns a count of all the players currently registered
	  6. registerPlayer(name)
	    * Takes a name string and adds a Player record to the database
	  7. playerStandings()
	    * Returns a list of players and their win records, sorted by most wins
	  8. reportMatch(winner, loser)
	    * Records a match result in the database. Takes in 2 player objects
	  9. swissPairings()
		* The main Swiss Pairing logic. Returns players list for match pairings

* **tournament_test.py** - supplied Unit Tests for Testing
	* Iterates through and tests against each of the tournament.py functions
	  1. Returns a printed Error indicated if a specific test has failed
	* If all TESTS succeed, you will receive a printed "Success! All tests pass!" message

## Installation:
#### System Requirements:
1. Python 2 (e.g. 2.7.x)
2. Postgresql 9 or higher

#### Obtaining the Code
* Clone the repository from GitHub
```
git clone https://github.com/nathandh/udacity-fullstack-tournament.git
```

#### Database Setup:
1. Import 'tournament.sql' database schema with 'psql' cli:
```
cd udacity-fullstack-tournament
psql
\i tournament.sql
```

#### Usage
To run:

1. Run the unit tests to test the implementation:
```
python tournament_test.sql
```

2. Validate that database has been updated during tests
* Launch the Postgres command line interface
* Connect to the tournament DB
* View records from PLAYER and MATCH tables
```
psql
\c tournament
select * from player;
select * from match;
```
