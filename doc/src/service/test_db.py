#!/usr/bin/python

DB_NAME = 'url_lookup_db'
TABLE_NAME = 'malacious_data'

config = {
  'user': 'root',
  'password': 'Root@123',
  'host': 'localhost',
  'raise_on_warnings': True,
}

TABLES = {}
TABLES['malacious_data'] = (
    "CREATE TABLE `malacious_data` ("
    " malacious_id int NOT NULL,"
    " `malacious` varchar(100) NOT NULL,"
    ") PRIMARY KEY (malacious_id), ENGINE=InnoDB")

print(TABLES)