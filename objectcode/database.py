import sqlite3   #importing sqlite3 library built in library for database in python 
conn=sqlite3.connect('Backend.sqlite')
cur=conn.cursor()
cur.execute("DROP TABLE IF EXISTS WordCount")
cur.execute("CREATE TABLE WordCounts(words Text,count Integer)")
lh=open('C:/Users/mayur g/Desktop/TerriblyTinyFiles.txt')      #textfile for reading
for line in lh:
               l=line.split()
               for i in range(len(l)):
                        s=l[i]
                        cur.execute("SELECT count FROM WordCounts where words=?",(s,))
                        row=cur.fetchone()
                        if row is None:
                                 cur.execute("INSERT INTO WordCounts(words,count) VALUES(?,1)",(s,))
                        else:
                                 cur.execute("UPDATE WordCount SET count=count+1 WHERE words=?",(s,))
                        conn.commit()
def view():
            sqlr="SELECT words,count FROM WordCounts ORDER BY count DESC LIMIT 10 "
            cur.execute(sqlr)
            rows=cur.fetchall()
            conn.commit()
            conn.close()
            return rows

view()   

# image for reference ![](https://github.com/Mayurg5899/TINYTALESASSIGNMENT/blob/master/images/2020-08-08%2017_47_18-Greenshotdatabase.png)
