import csv
import uuid
import mysql.connector


def connect_db():
  connection = mysql.connector.connect(host="localhost", user="root", passwd="")
  return connection


def create_database(connection):
  cursor = connection.cursor()
  query = "CREATE DATABASE IF NOT EXISTS ALX_prodev"
  cursor.execute(query)
  cursor.close()


def connect_to_prodev():
  connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="ALX_prodev")
  return connection


def create_table(connection):
  cursor = connection.cursor()
  query = """
        CREATE TABLE IF NOT EXISTS user_data (
      user_id VARCHAR(36) PRIMARY KEY,
      name VARCHAR(255) NOT NULL,
      email VARCHAR(255) NOT NULL,
      age INT(3) NOT NULL,
      CONSTRAINT unique_email UNIQUE (email)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci"""
  cursor.execute(query)


def insert_data(connection, data):
  with open(data, encoding='utf-8') as file:
    csv_reader = csv.reader(file, quotechar="'")
    next(csv_reader)

    batch = []
    for row in csv_reader:
      if len(row) < 3:
        continue
      name, email, age = row[0].strip('"'), row[1].strip('"'), row[2].strip('"')
      uuid_bytes = uuid.uuid4().bytes
      batch.append((str(uuid.UUID(bytes=uuid_bytes)), name, email, age))

    cursor = connection.cursor()
    query = """INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)"""
    cursor.executemany(query, batch)
    cursor.close()
