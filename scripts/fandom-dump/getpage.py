import sys, sqlite3
db = sqlite3.connect(sys.argv[1]); t = " ".join(sys.argv[2:])
r = db.execute("select title,redirect,text from pages where title=?", (t,)).fetchone()
if r and r[1]: r = db.execute("select title,redirect,text from pages where title=?", (r[1],)).fetchone()
print(r[2] if r else "NOT FOUND")
