import sqlite3
conn = sqlite3.connect('client_data.db')
c = conn.cursor()

def create_table():
    # need to get ALL parameters later
    c.execute('PRAGMA foreign_keys = ON;')
    c.execute('CREATE TABLE IF NOT EXISTS clients('
              'client_name TEXT PRIMARY KEY,'
              'email TEXT NOT NULL, '
              'income INTEGER NOT NULL)')
    c.execute('CREATE TABLE IF NOT EXISTS tags('
              'tag_name TEXT PRIMARY KEY)')
    c.execute('CREATE TABLE IF NOT EXISTS client_tags('
              'client TEXT NOT NULL, '
              'tag TEXT NOT NULL,'
              'FOREIGN KEY(client) REFERENCES client(client_name), '
              'FOREIGN KEY(tag) REFERENCES tags(tag_name));')

#won't crash if client is already in database
def enter_client(name, email, income):
    c.execute("SELECT client_name FROM clients WHERE client_name = ?",
              (name,))
    exists = c.fetchone()
    if exists:
        print("Client already exists")
    else:
        c.execute("INSERT INTO clients(client_name, email, income) VALUES(?,?,?)",
            (name, email, income))
        conn.commit()

def enter_tag (tag_name):
    #won't crash if tag is already in database
    c.execute("SELECT tag_name from tags WHERE tag_name = ?",
              (tag_name,))
    exists = c.fetchone()
    if exists:
        print("Tag already exists")
    else:
        c.execute("INSERT INTO tags(tag_name) VALUES(?)",
                  (tag_name,))
        conn.commit()

def enter_client_tag(client, tag):
    #not really sure if I'm doing this right...
    c.execute("SELECT client, tag FROM client_tags "
              "WHERE client = ? AND tag = ?",
              (client, tag))
    exists = c.fetchone()
    if exists:
        print(client + " has already been associated with " + tag + ".")
    else:
        c.execute("INSERT INTO client_tags(client, tag) VALUES(?,?)",
                  client, tag)
        conn.commit()