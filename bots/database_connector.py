#!/usr/bin/env python3
# TheOptomBot/bots/database_connector
# interacts with database to store data

import logging
import time
from datetime import datetime as dt
import sqlite3
from sqlite3 import Error

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# default functions for working with the database

def db_connect():
    connection = None 
    try: 
        connection = sqlite3.connect('database.db')
        # logger.info('Connection to database successful')
    except Error as e: 
        logger.error(f'Error connecting to database: {e}')
    return connection

def ex_query(query, params={}):
    connection = db_connect()
    cursor = connection.cursor()
    try:
        cursor.execute(query, params)
        connection.commit()
        logger.info('Query successful')
    except Error as e:
        logger.error(f'Error executing query: {e}')
    return

def read_query(query, params={}):
    connection = db_connect()
    cursor = connection.cursor()
    result = None
    try: 
        cursor.execute(query, params)
        result = cursor.fetchall()
        logger.info('Read Query successful')
    except Error as e:
        logger.error(f'Error executing query: {e}')
    return

# custom function to work with the script

def create_db():
    query = """
    CREATE TABLE IF NOT EXISTS stop_spam(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tweethash NUMBER NOT NULL
        );
    """
    ex_query(query)
    return

def store_tweet(tweet):
    # since the value is hash'd
    # SQL injection is not likely but
    # still good practice
    query = """
    INSERT INTO stop_spam(
        tweethash
        )
    VALUES
        (:tweethash
        )
    """
    params = {
        'tweethash': hash(tweet.text),
            }
    ex_query(query, params)
    return

def check_tweet(tweet):
    """
    return True if tweet hash already exists; False otherwise
    """
    query = """
    SELECT tweethash
    FROM stop_spam
    WHERE tweethash=(
    :tweethash
    )
    """
    params = {
        'tweethash': hash(tweet.text)
            }
    if read_query(query, params):
        return True
    return False
