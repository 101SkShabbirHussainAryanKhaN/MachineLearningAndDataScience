import mysql.connector
from config import db_config

# # create connection
# def create_connection():
#     try:
#         connection = mysql.connector.connect(**db_config)
#         if connection.is_connected:
#             print('connected')
#             return connection
#     except mysql.connector.Error as err:
#         print(f"Error : {err}")
#         return None
        


# def close_connection(connection):
#     if connection:
#         connection.close()
#         print("Database connection closed")

def create_table():
    connection = create_connection()
    cursor = None  # Initialize the cursor variable

    try:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS student_dbms1(std_id INT PRIMARY KEY AUTO_INCREMENT, reg_no varchar(100) not null, std_name VARCHAR(100) NOT NULL, std_email VARCHAR(100) NOT NULL, std_contact int not null, std_dob varchar(50) not null, hostelite varchar(100) not null, image_data BLOB)')
    except Exception as err:
        print(f"An error occurred: {err}")
    finally:
        if cursor:
            cursor.close()
        close_connection(connection)

