import sqlite3

with sqlite3.connect("DataBase/users.db") as connection:
    c = connection.cursor()

    c.execute("create table if not exists users (id integer primary key, nickname text not null)")

    connection.commit()
    