import sqlite3 as sql
from aiogram.utils.markdown import hlink
def user(id):
    con = sql.connect('users.db')
    with con:
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS `users` (id INT PRIMARY KEY, Nick TEXT, ref INT)")
        info = cur.execute(f"SELECT * FROM users WHERE id=('{id}')")
        return info.fetchone()
    con.commit()
    cur.close()

def top():
    con = sql.connect("users.db")
    with con:
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS `users` (id INT PRIMARY KEY, Nick TEXT, ref INT)")
        tops=cur.execute(f'SELECT * FROM users ORDER BY ref DESC').fetchall()
    con.commit()
    cur.close()
    spisoks=''
    k=1
    for name in tops:
        if k<=10:
            link=hlink(name[1], 'tg://user?id='+str(name[0]))
            spisoks=spisoks+ '\n' + f'{k})' + f'{link}[<code>{name[0]}</code>]  -  {name[2]}'
            k+=1
        if k>10:
            break
    return spisoks

def spisok():
    con = sql.connect("users.db")
    with con:
        cur = con.cursor()
        cur.execute(f"SELECT id, Nick FROM users")
        results = (cur.fetchall())
        return results
    con.commit()
    cur.close()

def add_ref(id):
    con = sql.connect("users.db")
    info1= user(id)
    with con:
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS `users` (id INT PRIMARY KEY, Nick TEXT, ref INT)")
        info = user(id)[2]
        cur.execute(f'UPDATE users SET ref={info+1} WHERE id={id}')
        return f''
    con.commit()
    cur.close()
def select_all_users():
    conn = sql.connect('users.db', check_same_thread=False)
    cursor = conn.execute(f"SELECT COUNT(*) as count FROM users")
    h = cursor.fetchall()
    conn.close()
    return h[0][0]

def ref(message):
	con = sql.connect("users.db")
	with con:
		cur = con.cursor()
		id = message.from_user.id
		cursor = cur.execute(f"SELECT ref FROM users WHERE id={id}")
		hh = cursor.fetchall()
		return hh[0][0]
	con.commit()
	cur.close()
	
 
 