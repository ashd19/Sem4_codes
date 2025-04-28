import sqlite3

conn = sqlite3.connect("pylab_56.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    )
""")

def create_user(name, age):
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()

def read_users():
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

def update_user(user_id, name, age):
    cursor.execute("UPDATE users SET name = ?, age = ? WHERE id = ?", (name, age, user_id))
    conn.commit()

def delete_user(user_id):
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()


create_user("Naitik", 56)
create_user("Atharva", 53)

print("All Users:", read_users())

update_user(1, "Naitik Mehta", 26)

delete_user(2)

print("After Updates:", read_users())

conn.close()
