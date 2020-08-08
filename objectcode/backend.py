import sqlite3
def view():
            conn=sqlite3.connect('Backend.sqlite')
            cur=conn.cursor()
            sqlr="SELECT words,count FROM WordCounts ORDER BY count DESC"
            cur.execute(sqlr)
            rows=cur.fetchall()
            conn.commit()
            conn.close()
            return rows
view()
