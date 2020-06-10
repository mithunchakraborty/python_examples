    import psycopg2
    from contextlib import closing

def main() :
    with closing(psycopg2.connect(
        dbname="agency",
        user="postgres",
        password="postgres",
        host="localhost"
    )) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM position")
            for row in cursor:
                print(row)

if __name__ == "__main__" :
    main()

#records = cursor.fetchall()
#cursor.fetchone() — возвращает 1 строку
#cursor.fetchall() — возвращает список всех строк
#cursor.fetchmany(size=5) — возвращает заданное количество строк

# cursor итерируется
#for row in cursor:
#    print(row)

# словарь
# with conn.cursor(cursor_factory=DictCursor) as cursor:

# Чтобы динамически подставлять таблицу
#from psycopg2 import sql
#>>> with conn.cursor() as cursor:
#        columns = ('country_name_ru', 'airport_name_ru', 'city_code')
#        stmt = sql.SQL('SELECT {} FROM {} LIMIT 5').format(
#            sql.SQL(',').join(map(sql.Identifier, columns)),
#            sql.Identifier('airport')
#        )
#        cursor.execute(stmt)
#        for row in cursor:
#            print(row)

#Транзакции
#with conn.cursor() as cursor:
#    conn.autocommit = True
#    values = [
#        ('ALA', 'Almaty', 'Kazakhstan'),
#        ('TSE', 'Astana', 'Kazakhstan'),
#        ('PDX', 'Portland', 'USA'),
#    ]
#    insert = sql.SQL('INSERT INTO city (code, name, country_name) VALUES {}').format(
#        sql.SQL(',').join(map(sql.Literal, values))
#    )
#    cursor.execute(insert)

#Удаленное соединение. ssh-туннель
#from sshtunnel.sshtunnel import SSHTunnelForwarder
#PORT = 5432
#with SSHTunnelForwarder(
#    (REMOTE_HOST, REMOTE_SSH_PORT),
#    ssh_username=REMOTE_USERNAME,
#    ssh_password=REMOTE_PASSWORD,
#    remote_bind_address=("localhost", PORT),
#    local_bind_address=("localhost", PORT)
#) :
#    conn = ...
