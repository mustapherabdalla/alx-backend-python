import mysql.connector

def stream_user_ages():
    connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="ALX_prodev")
    cursor = connection.cursor()
    query = "SELECT age FROM user_data WHERE 1"
    cursor.execute(query)
    ages = cursor.fetchall()
    for (age,) in ages:
        yield age
    return None


def calculate_average():
    total = 0
    ages = stream_user_ages()
    for age in ages:
        total = total + age

    average = total / len(ages)
    print("Average age of users: ", average)

calculate_average()
