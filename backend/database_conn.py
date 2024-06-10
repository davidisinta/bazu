import psycopg2
from psycopg2.extras import RealDictCursor
import time

def connect_to_database():
    ## database connection
    DB_NAME = "bazunu_db"
    DB_USER = "postgres"
    DB_PASSWORD = "hardToguess73"
    DB_HOST = "localhost"
    DB_PORT = "5432"

    while True:
        try:
            conn = psycopg2.connect(
                host=DB_HOST,
                port=DB_PORT,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD,
                cursor_factory=RealDictCursor
            )

            cursor = conn.cursor()

            print("----------------------------------------------------------------")
            print("Connected to Database successfully!!")
            print("----------------------------------------------------------------")
            break

        except Exception as e:
            print("----------------------------------------------------------------")
            print("Failed to Connect to Database")
            print(e)
            print("----------------------------------------------------------------")
            time.sleep(10)

if __name__ == "__main__":
    connect_to_database()
