import functools
import time
import mysql.connector


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


def retry_on_failure(retries, delay):
    def decorator(func):
        # noinspection PyInconsistentReturns
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)

                except Exception as e:
                    last_exception = e
                    if attempt < retries:
                        print(f"Attempt {attempt} failed. Retrying in {delay} seconds")
                        time.sleep(delay)
            print(f"All {retries} attempts failed. Last error: {last_exception}")
        return wrapper
    return decorator


@with_db_connection
@retry_on_failure(retries=3, delay=2)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure
users = fetch_users_with_retry()
print(users)
