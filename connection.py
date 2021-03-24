from sqlite3 import connect;

connection = connect('DATABASE_NAME_HERE')

cursor = connection.cursor()

# SQL QUERIES
query = cursor.execute('SQL_QUERY_HERE')
rows = query.fetchall() 

connection.close() # Also works with Python "with" environment