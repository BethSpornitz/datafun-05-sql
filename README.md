# datafun-05-sql

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
