import os

import mysql.connector
# from mysql import connector
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

#print(os.getenv('USER'))
user = os.getenv('USER')
password = os.getenv('PASSWORD')
host = os.getenv('HOST')
database = 'swiftmarket'

password

connection = mysql.connector.connect(user=user,
                                     password=password,
                                     host=host,
                                     database=database )

cursor = connection.cursor()

# to read sql query
def read_query(query):
    """Reading sql """
