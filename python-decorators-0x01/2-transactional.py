import functools
import mysql.connector
from mysql.connector import IntegrityError


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


def transactional(func):
    @functools.wraps(func)
    def wrapper(connection, *args, **kwargs):
        try:
            cursor = connection.cursor()
            cursor.execute("START TRANSACTION")
            result = func(connection, *args, **kwargs)
            connection.commit()
            return result

        except IntegrityError as e:
            print("Integrity Error: ", e)
            return None

        except Exception as e:
            connection.rollback()
            print("transaction failed: ", e)
            return None

    return wrapper


@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    cursor = conn.cursor()
    cursor.execute("UPDATE user_data SET email = %s WHERE user_id = %s", (new_email, user_id))

#### Update user's email with automatic transaction handling
update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')
