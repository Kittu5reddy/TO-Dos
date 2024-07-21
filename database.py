import sqlite3


conn=sqlite3.connect('database.db')
conn.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    password TEXT NOT NULL,
      email text not null
);
''')


# conn.execute('''
# CREATE TABLE todo (
#     dateofcre Date not null,
#     name TEXT NOT NULL,
#     description TEXT NOT NULL
# );
# ''')
