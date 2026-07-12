import psycopg

conn = psycopg.connect(
    host="localhost",
    dbname="wallet",
    user="postgres",
    password=" ",
    port=5432
)
##Write data
#cur.execute("INSERT INTO students (name, age) VALUES (%s, %s)",("Alice", 20))
#conn.commit()

##read data
#cur.execute("SELECT * FROM students")
#rows = cur.fetchall()
#for row in rows:
#    print(row)
conn.close()