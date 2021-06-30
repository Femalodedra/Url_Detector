#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
from src.lib.test_db import DB_NAME
from src.lib.test_db import config
import mysql.connector
from mysql.connector import errorcode

import logging
logger = logging.getLogger(__name__)


class URL_Detector:

    def __init__(self, URL):
        self.URL = URL

    def URL_Search(self):
        """
        Regex to see different types of URL
        """
        regex = r'^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$'

        # check input URL along with database
        reg_val = re.search(regex, self.URL)

        web = ""
        BadURL = True
        if reg_val:
            if reg_val.group(2) is not None:
                web = reg_val.group(2).strip(r'www\d?.')
            if reg_val.group(3) is not None:
                com = reg_val.group(3)
            web = "{0}.{1}".format(web, com)
        else:
            print("Try with the good url format (http://www.microsof.com)")
            raise

        # Establish the connection for database and see if the web is in list of malacious_data
        con = mysql.connector.connect(**config)
        print("Retrieving from the database.....")
        cursor = con.cursor()
        try:
            con.database = DB_NAME
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Authentication Error, try again with the correct username and password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("The Database is not available")
            else:
                print(err)
                exit(1)

        logger.info("The database Connection is Successful")

        query = "SELECT COUNT(*) FROM malacious_data where malacious = '{0}'".format(web)
        logger.info("The search query is", query)
        cursor.execute(query)
        BadURL, = cursor.fetchone()

        """
        with open("resouce/mal_content.txt") as f:
            for line in f:
                if re.search(web, line):
                    BadURL = False
                    break
        """

        # Response
        if BadURL:
            return True
        else:
            return False