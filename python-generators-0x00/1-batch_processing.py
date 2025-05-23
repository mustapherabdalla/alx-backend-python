import mysql.connector

def stream_users_in_batches(batch_size):
    connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="ALX_prodev")
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM user_data"
    cursor.execute(query)
    rows = cursor.fetchall()

    for i in range(0, len(rows), batch_size):
        batches = rows[i: i + batch_size]
        results = [batch for batch in batches]
        return results
    return None

def batch_processing(batch_size):
    batches = stream_users_in_batches(batch_size)

    for batch in batches:
        for i in range(0, len(batch)):
            user = batch[i]
            if user['age'] > 25:
                continue
            print(user)
        print("\n\n")

