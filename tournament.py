# Nathan D. Hernandez
# Udacity FullStack NanoDegree
# ver: 0.1 - 05/2017
#
# !/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#


import psycopg2
import random


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def close_connection(cursor, db):
    cursor.close()
    db.close()


def deleteMatches():
    """Remove all the match records from the database."""
    connection = connect()
    c = connection.cursor()
    c.execute("DELETE FROM match;")
    connection.commit()

    close_connection(c, connection)


def deletePlayers():
    """Remove all the player records from the database."""
    connection = connect()
    c = connection.cursor()
    c.execute("DELETE FROM player;")
    connection.commit()

    close_connection(c, connection)


def countPlayers():
    """Returns the number of players currently registered."""
    connection = connect()
    c = connection.cursor()
    c.execute("SELECT COUNT(*) FROM player;")
    count = c.fetchone()[0]

    # print "Count is: %s" % count
    close_connection(c, connection)
    return count


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    connection = connect()
    c = connection.cursor()
    c.execute("INSERT INTO player VALUES (DEFAULT, %s, DEFAULT);", (name,))
    connection.commit()

    close_connection(c, connection)


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    connection = connect()
    c = connection.cursor()
    c.execute("""SELECT p.id, p.name, (SELECT COUNT(*) FROM match WHERE p.id =
winner) AS wins, (SELECT COUNT(*) FROM match WHERE p.id = winner OR p.id =
loser) AS matches FROM player as p ORDER BY wins desc;""")
    standings = c.fetchall()
    # print standings

    close_connection(c, connection)
    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    connection = connect()
    c = connection.cursor()
    c.execute("INSERT INTO match VALUES (DEFAULT, %s, %s, DEFAULT);",
              (winner, loser))
    connection.commit()

    close_connection(c, connection)


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    swiss_pairings = []

    standings = playerStandings()

    winners_list = []
    for standing in standings:
        if standing[2] > 0:
            winners_list.append(standing)
    print "Winner's list is: %s" % winners_list

    connection = connect()
    c = connection.cursor()
    c.execute("SELECT * FROM player;")
    players = c.fetchall()

    close_connection(c, connection)

    if len(winners_list) == 0:
        # Generate matches based off of all 'players'
        pair_tracker = []
        count = 0
        for x in range(0, len(players)):
            # print "X is: %s" % x
            # print players[x]
            if x not in pair_tracker:
                rand_idx = None
                while rand_idx is None:
                    rand_idx = random.randrange(0, len(players))
                    if (rand_idx in pair_tracker) or (rand_idx == x):
                        """ print "Skipping current random idx: %s |
                            curr_idx: %s" % (rand_idx, x)"""
                        rand_idx = None
                    else:
                        # print "rand_idx is: %s" % rand_idx
                        pair_tracker.append(rand_idx)
                curr_player = players[x]
                opponent_player = players[rand_idx]

                swiss_pairings.append((curr_player[0], curr_player[1],
                                       opponent_player[0], opponent_player[1]))

                pair_tracker.append(x)
    else:
        # print "We have winner's so pairing accordingly..."
        # Pair with player of next win rank next to them
        # We use 'standings' here to generate matches
        count = 0
        for x in range(0, len(standings), 2):
            curr_player = standings[x]
            opponent_player = standings[x+1]
            swiss_pairings.append((curr_player[0], curr_player[1],
                                   opponent_player[0], opponent_player[1]))

    print "Pairings are: %s" % swiss_pairings
    return swiss_pairings
