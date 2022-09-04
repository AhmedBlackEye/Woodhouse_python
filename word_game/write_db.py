import sqlite3

conn = sqlite3.connect('words_db.db')

c = conn.cursor()

create_table_sql = """CREATE TABLE dictionary (
    INTEGER PRIMARY KEY,
    key_word text,
    synonym text,
    antonym text
);"""

c.execute(create_table_sql)
conn.commit()

with open("orginal.txt", "r", encoding='utf8') as file:
    page = file.read()
    blocks = page.split("=")
    count=1
    err = 0
    for block in blocks:
        lines = block.strip().split('\n')
        if len(lines) != 5: continue
        try:
            c.execute(f"INSERT INTO dictionary VALUES ({count},'{lines[0][4:]}', '{lines[2][4:]}', '{lines[4][4:]}')")
        except:
            err+=1
            continue
        count+=1

conn.commit()
conn.close()

print(err, count)