import json
import sqlite3 as sql

db = sql.connect("database.db")
cur = db.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS user(
    id INTEGER PRIMARY KEY,
    tg_id INTEGER,
    user TEXT,
    keys INTEGER
)
""")
cur.execute("""
CREATE TABLE IF NOT EXISTS pages(
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    url TEXT,
    FOREIGN KEY(user_id) REFERENCES user(id)
)
""")
db.commit()


def create_user(user):
    is_user = cur.execute("SELECT * FROM user WHERE tg_id = ?", (user.id,)).fetchone()
    if not is_user:
        user_data = {"username": user.username, "first_name": user.first_name, "last_name": user.last_name}
        cur.execute("INSERT INTO user(tg_id, user, keys) VALUES(?,?,?)", (user.id, json.dumps(user_data), 0,))
        db.commit()
        return "Created"
    return "IsHave"


def create_page(user_id, url):
    cur.execute("INSERT INTO pages(user_id, url) VALUES(?,?)", (user_id, url,))
    return True


def get_page(*args, **kwargs):
    if kwargs.get("filter"):
        if not kwargs.get("user_id"):
            return "user_id are required"

        pages = cur.execute("SELECT * FROM pages WHERE user_id = ?", (kwargs["user_id"],)).fetchall()
        return pages


print(get_page(filter="user_pages"))
