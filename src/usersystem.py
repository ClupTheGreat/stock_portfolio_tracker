import sqlite3
import hashlib

conn = sqlite3.connect("./data/userdata.db")
cur = conn.cursor()

cur.execute("""
            CREATE TABLE IF NOT EXISTS userdata (id INTEGER PRIMARY KEY, 
                                                 username VARCHAR(255) NOT NULL,
                                                 password VARCHAR(255) NOT NULL
            )
            """)

def register(username, password):
    if username != " " and username != None and password != " " and password != None:
        cur.execute("""SELECT username FROM userdata WHERE username = ?""", (username,))
        if cur.fetchone() == None:
            password = hashlib.sha256(password.encode()).hexdigest()
            cur.execute("""
                INSERT INTO userdata (username, password) VALUES (?, ?)
            """,(username, password))
            conn.commit()
            return True
        else:
            return False
    else:
        return False

def login(username, password):
    if username != " " and username != None and password != " " and password != None:
        password = hashlib.sha256(password.encode()).hexdigest()
        cur.execute("""SELECT username, password FROM userdata WHERE username = ? AND password = ?""",(username,password))
        if cur.fetchone() == None:
            return False,username
        else:
            return True,username


# print(register("Rohansssz", "Topno"))
# print(hashlib.sha256("Topno".encode()).hexdigest()=="aa0f942e54bdf31d5ecf38fd5a35059256470c31d2c471f1201e79e3fb51e25e")
# print(login("Rohan","Topno"))
conn.commit()