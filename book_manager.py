import sqlite3
import pathlib
import pandas as pd

# Define paths using joinpath
db_file_path = pathlib.Path("project.db")
sql_file_path = pathlib.Path("sql") / "create_tables.sql"
author_data_path = pathlib.Path("data") / "authors.csv"
book_data_path = pathlib.Path("data") / "books.csv"

def verify_and_create_folders(paths):
    """Verify and create folders if they don't exist."""
    for path in paths:
        folder = path.parent
        if not folder.exists():
            print(f"Creating folder: {folder}")
            folder.mkdir(parents=True, exist_ok=True)
        else:
            print(f"Folder already exists: {folder}")

def create_database(db_file_path):
    """Create a new SQLite database file if it doesn't exist."""
    try:
        conn = sqlite3.connect(db_file_path)
        conn.close()
        print("Database created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating the database: {e}")

def create_tables(db_file_path, sql_file_path):
    """Read and execute SQL statements to create tables."""
    try:
        with sqlite3.connect(db_file_path) as conn:
            with open(sql_file_path, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Tables created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")

def insert_data_from_csv(db_file_path, author_data_path, book_data_path):
    """Read data from CSV files and insert the records into their respective tables."""
    try:
        # Verify that the CSV files exist and are not empty
        if not author_data_path.exists():
            raise FileNotFoundError(f"{author_data_path} does not exist")
        if not book_data_path.exists():
            raise FileNotFoundError(f"{book_data_path} does not exist")

        authors_df = pd.read_csv(author_data_path)
        books_df = pd.read_csv(book_data_path)

        print(f"Authors DataFrame:\n{authors_df.head()}")
        print(f"Books DataFrame:\n{books_df.head()}")

        with sqlite3.connect(db_file_path) as conn:
            authors_df.to_sql("authors", conn, if_exists="replace", index=False)
            books_df.to_sql("books", conn, if_exists="replace", index=False)
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print(f"Error inserting data: {e}")

def main():
    paths_to_verify = [sql_file_path, author_data_path, book_data_path]
    verify_and_create_folders(paths_to_verify)

    create_database(db_file_path)
    create_tables(db_file_path, sql_file_path)
    insert_data_from_csv(db_file_path, author_data_path, book_data_path)

if __name__ == "__main__":
    main()
