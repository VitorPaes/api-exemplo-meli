import psycopg2
import csv

conn = psycopg2.connect(database="root", user="root", password="root",port="5439",host="localhost",keepalives=1,
                        keepalives_idle=130,
                        keepalives_interval=10,
                        keepalives_count=15)
cur = conn.cursor()
with open('MELI_smart_tv_results.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) 
    for row in reader:
        cur.execute(
        "INSERT INTO items VALUES (%s, %s, %s, %s,%s,%s)",
        row
    )
conn.commit()

# Dados carregados
cur.execute("select count(1) from items")
results = cur.fetchone()
print(f"Carregado na tabela Items com {results[0]} registros!")