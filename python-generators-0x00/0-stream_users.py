import mysql.connector


def stream_users():
    connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="ALX_prodev")
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM user_data"
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        yield row

