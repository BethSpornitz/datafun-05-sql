# Project 5 SQL Module
Project 5 integrates Python and SQL, focusing on database interactions using SQLite. This project introduces logging, a useful tool for debugging and monitoring projects, and involves creating and managing a database, building a schema, and performing various SQL operations, including queries with joins, filters, and aggregations.

# Create and Activate Project Virtual Environment
py -m venv .venv  
.venv\Scripts\Activate

# Add and Commit Changes to Github
git add .
git commit -m
git push -u origin main

# Add external dependencies
pip install pandas
pip install pyarrow

# Create files
.gitignore
README.md
requirements.txt
data folder with authors.csv and books.csv (with their data inside the file)  
SQL folder with a file called create_tables.sql  
book_manager.py (for Python code)  
project.db (database file created using Python code)  
