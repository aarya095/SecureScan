import mysql.connector
import os
from mysql.connector import Error

class DatabaseConnection:
    def __init__(self):

        self.host = os.getenv('DB_HOST') #env: environment variables
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')
        self.database = os.getenv('DB_NAME')
        self.connection = None

    def connect_to_database(self):

        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Successfully connected to database.")
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            self.connection = None

    def close_connection(self):

        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Connection closed.")

    def get_connection(self):

        return self.connection

    def execute_query(self, query, params=None):

        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()
        cursor.close()

    def fetch_all(self, query, params=None):

        cursor = self.connection.cursor()
        cursor.execute(query, params)
        result=cursor.fetchall()
        cursor.close()
        return result