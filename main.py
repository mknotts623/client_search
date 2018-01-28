import sqlite3
conn = sqlite3.connect('client_data.db')
c = conn.cursor()

def PRAGMA_keys():
    c.execute('PRAGMA foreign_keys')

def create_table():
    # need to get ALL parameters later
    c.execute('PRAGMA foreign_keys = ON;')
    c.execute('CREATE TABLE IF NOT EXISTS clients('
              'client_id INTEGER NOT NULL, '
              'client_name TEXT PRIMARY KEY,'
              ' email TEXT NOT NULL, '
              'income INTEGER NOT NULL);')
    c.execute('CREATE TABLE IF NOT EXISTS tags('
              'tag_id INTEGER NOT NULL, '
              'tag_name TEXT PRIMARY KEY);')
    c.execute('CREATE TABLE IF NOT EXISTS client_tags('
              'client TEXT NOT NULL, '
              'tag TEXT NOT NULL,'
              'FOREIGN KEY(client) REFERENCES client(client_name), '
              'FOREIGN KEY(tag) REFERENCES tags(tag_name));')

def enter_client(name, email, income):
    #need to get ALL parameters later
    c.execute("INSERT INTO clients(name, email, income) VALUES(?,?,?)", (name, email, income))
    conn.commit()
    c.close()
    conn.close()

#test execute statements
PRAGMA_keys()
create_table()