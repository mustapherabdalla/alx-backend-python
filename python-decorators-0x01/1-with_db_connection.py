import mysql.connector
import functools


def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="ALX_prodev")
        try:
            return func(connection, *args, **kwargs)
        except Exception as e:
            print(f"Database error: {e}")
            raise
        finally:
            connection.close()

    return wrapper

@with_db_connection
def get_user_by_id(connection, user_id):
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM user_data WHERE user_id = {user_id}")
    return cursor.fetchone()


#### Fetch user by ID with automatic connection handling
user = get_user_by_id(user_id=1)
print(user)
