# import sqlite3
#
# # Connect to the SQLite database
# conn = sqlite3.connect("myrecipes.db")
# cursor = conn.cursor()
#
# # Define the SQL command to create the 'users' table
# create_users_table = """
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY,
#     username TEXT NOT NULL,
#     email TEXT,
#     age INTEGER,
#     password TEXT NOT NULL
# );
# """
# conn.execute(create_users_table)
#
# print("Table got created")
# conn.commit()
# #
# # # Execute the SQL command
# # cursor.execute(create_users_table)
# #
# # # Commit changes and close the connection
# # conn.commit()
# # conn.close()
# #
# # print("The 'users' table has been created successfully.")
#
# # import sqlite3
# # import time
# #
# # def execute_query_with_retry(query):
# #     conn = sqlite3.connect('example.db')
# #     cursor = conn.cursor()
# #     attempts = 0
# #     while attempts < 3:  # Retry up to 3 times
# #         try:
# #             cursor.execute(query)
# #             conn.commit()
# #             conn.close()
# #             return
# #         except sqlite3.OperationalError as e:
# #             print(f"SQLite error: {e}. Retrying...")
# #             attempts += 1
# #             time.sleep(1)  # Wait for 1 second before retrying
# #     print("Failed after 3 attempts. Check database status.")
# #
# # # Example usage:
# # query = "INSERT INTO table_name (column1, column2) VALUES ('value1', 'value2')"
# # execute_query_with_retry(query)
# # import sqlite3
# #
# # conn = sqlite3.connect('mydatabase.db',timeout=20)
# # try:
# #     cursor = conn.cursor()
# #     print("Database got connected")
# #     # Perform database operations here
# #     conn.commit()  # Commit the transaction
# # except sqlite3.Error as e:
# #     print("SQLite error:", e)
# #     conn.rollback()  # Rollback the transaction on error
# # finally:
# #     conn.close()  # Always close the connection

# import bcrypt
#
# def hash_password(password):
#     # Hash the password using bcrypt
#     salt = bcrypt.gensalt()
#     hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
#     return hashed_password
#
# def verify_password(stored_hashed_password, provided_password):
#     return bcrypt.checkpw(provided_password.encode("utf-8"), stored_hashed_password)
#
# # Example usage
# stored_hashed_password = b"$2b$12$..."
# provided_password = "mysecretpassword"
#
# if verify_password(stored_hashed_password, provided_password):
#     print("Password verified! User can log in.")
# else:
#     print("Incorrect password.")

# import bcrypt
#
#
# def check_password_match(provided_password, stored_hashed_password):
#     try:
#         # Decode the stored hashed password
#         stored_hashed_password = stored_hashed_password.encode("utf-8")
#
#         # Check if the provided password matches the stored hashed password
#         return bcrypt.checkpw(provided_password.encode("utf-8"), stored_hashed_password)
#     except Exception as e:
#         return str(e)
#
#
# # Example usage
# provided_password = "mysecret"
# stored_hashed_password = ("$2b$12$u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6"
#                           "ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ7e9z2e6j9j2J5u6ZQ")

import secrets
import string

def generate_secret_key(length=24):
    alphabet = string.ascii_letters + string.digits + '!@#$%^&*(-_=+)'
    return ''.join(secrets.choice(alphabet) for _ in range(length))

# Generate a secret key
secret_key = generate_secret_key()
print(secret_key)