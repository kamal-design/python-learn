# Data base connectivity
# MySQL
# PostgreSQL
# SQLite
# MongoDB
# Oracle
# SQL Server


# Terminal cmd line to connect to mysql DB
# mysql -u root
# mysql -u root -D python_db
# mysql -u root -p
# SHOW DATABASES;
# USE python_db;
# SHOW TABLES;
# SELECT * FROM users;
# EXIT;



# pip install mysql-connector-python
import pymysql

# STEP:1 connect to database
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="", # root user local "", remote "root"
    # database="python_db" # Make sure database is exists, if not exists create it
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:
        # Check Database
        cursor.execute("CREATE DATABASE IF NOT EXISTS python_db")
        cursor.execute("USE python_db")
        # create table users
        # cursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), email VARCHAR(100))")

        # STEP:2 create a table
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100),
            department VARCHAR(100)
        );
        """
        cursor.execute(create_table_query)

        # STEP:3 Insert data
        # cursor.execute("INSERT INTO users (name, email, department) VALUES ('Kamal', 'kamal@example.com', 'IT')")
        # cursor.executemany("INSERT INTO users (name, email, department) VALUES (%s, %s, %s)", [('Kamal', 'kamal@example.com', 'IT'), ('John', 'john@example.com', 'HR')])
        # connection.commit()

        insert_query = "INSERT INTO users (name, email, department) VALUES (%s, %s, %s)"
        data_values = [('Kamal', 'kamal@example.com', 'IT'), ('John', 'john@example.com', 'HR')]
        cursor.executemany(insert_query, data_values)
        connection.commit()

        # STEP:4 select query Data
        select_query = "SELECT * FROM users"
        cursor.execute(select_query)
        result = cursor.fetchall()
        print("\n All Data:", result, "\n")

        # file handling
        with open("users.txt", "w") as f:
            for row in result:
                f.write(f"{row}\n")
                print("\n Row: ",row)

        # STEP:5 update query
        # update_query = "UPDATE users SET name = 'Kamal' WHERE id = 1"
        # cursor.execute(update_query)
        # connection.commit()
        # print("Updated")

        # STEP:6 delete query
        # delete_query = "DELETE FROM users WHERE id = 1"
        # cursor.execute(delete_query)
        # connection.commit()
        # print("Deleted")
except Exception as e:
    print(e)
finally:
    connection.close()
    print("Connection closed")
