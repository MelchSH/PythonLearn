import sqlite3

connection = sqlite3.connect("mydata.db")

# Need cursor to use commands
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS persons (
    first_name TEXT, 
    last_name TEXT,
    age INTEGER              
)               
""")

cursor.execute("""
INSERT INTO persons VALUES 
("Romy", "Soto", 8),
("Maya", "Soto", 4),
("Mash"," ",21)
""")

cursor.execute("""
SELECT * FROM persons WHERE last_name = "Soto"
""")

rows = cursor.fetchall()
print(rows)

connection.commit()
connection.close()

