import mysql.connector


def paginate_users(page_size, offset):
    connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="ALX_prodev")
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    return rows


def lazy_paginate(page_size):
    offset = 0
    current_page = paginate_users(page_size, offset)

    for i in range(len(current_page)):
        if not current_page:
                break
        yield current_page
