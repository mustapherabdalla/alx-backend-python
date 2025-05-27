import functools
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


query_cache = {}

def cache_query(func):
    @functools.wraps(func)
    def wrapper(connection, query, *args, **kwargs):
        if query in query_cache:
            print("Query already cached")
            return query_cache[query]

        result = func(connection, query, *args, **kwargs)
        query_cache[query] = result
        print("Cached new query")
        return result
    return wrapper


@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM user_data")
#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM user_data")
