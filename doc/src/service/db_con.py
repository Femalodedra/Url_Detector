from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode
from src.lib.test_db import TABLES
from src.lib.test_db import DB_NAME
from src.lib.test_db import config

import logging
logger = logging.getLogger(__name__)


def tables(cursor, link):
    for name, ddl in TABLES.iteritems():
        try:
            logger.info("Creating table {}: ".format(name), end='')
            cursor.execute(ddl)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                logger.error("already exists.")
            else:
                logger.error(err.msg)
        else:
            print("OK")

    cursor.close()
    link.close()


def database_in(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("The database creation is unsuccessful: {}".format(err))
        exit(1)


def main():
    con = mysql.connector.connect(**config)
    cursor = con.cursor()

    try:
        con.database = DB_NAME

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Authentication Error, try again with the correct username and password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("The Database is not available")
            database_in(cursor)
            con.database = DB_NAME

        else:
            print(err)
            exit(1)

    logger.warning("Successful connection")
    cursor.execute("DROP TABLE IF EXISTS malacious_data")
    sql = """CREATE TABLE malacious_data (malacious TEXT)"""
    cursor.execute(sql)
    con.commit()

    with open("resouce/mal_content.txt") as f:
        for site in f:
            site = site.strip('\n')
            cursor.execute('''INSERT INTO malacious_data (malacious) VALUES ("{0}")'''.format(site))

    """
    with open("resouce/mal_content.txt") as f:
        for line in f:
            cursor.execute(add_mal, line)
    """
    con.commit()

    cursor.execute("""SELECT * FROM malacious_data;""")
    data = (cursor.fetchall())
    print(data)
    cursor.close()
    con.close()


if __name__ == "__main__":
    main()