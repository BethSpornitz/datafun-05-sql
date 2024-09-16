import sqlite3

# Path to the new database file
db_file_path = 'project.db'

# Create a new SQLite database or connect to an existing one
conn = sqlite3.connect(db_file_path)

# Create a new SQLite cursor
cur = conn.cursor()


# Commit the transaction (if any changes were made)
conn.commit()

# Close the connection
conn.close()

print(f"Database '{db_file_path}' created successfully.")