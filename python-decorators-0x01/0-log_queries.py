import mysql.connector

def log_queries():
    def decorator(func):
        def wrapper(query, *args, **kwargs):
            print(query)
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
