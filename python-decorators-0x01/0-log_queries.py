import mysql.connector
from _datetime import datetime


def log_queries():
    def decorator(func):
        def wrapper(query, *args, **kwargs):
            time_executed = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(query, "executed at: ", time_executed)
            return func(query, *args, **kwargs)
        return wrapper
    return decorator

@log_queries()
def fetch_all_users(query):
    connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="ALX_prodev")
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    connection.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM user_data")
