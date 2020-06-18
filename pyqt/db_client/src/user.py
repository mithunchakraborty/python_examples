import psycopg2
from contextlib import closing

class User(object) :
    def __init__(self, login:str, password:str) :
        self.login = login
        self.password = password

    def getNamesTables(self) :
        with closing(psycopg2.connect(
            dbname="agency",
            user=self.login,
            password=self.password,
            host="localhost"
        )) as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """ SELECT table_name
                        FROM information_schema.tables
                        WHERE table_schema NOT IN
                        ('information_schema', 'pg_catalog')
                        AND table_schema IN('public', 'agency');
                    """
                )
                result = []
                for row in cursor: result += row

                return result

    def selectFromTable(self, table="department") :
        with closing(psycopg2.connect(
            dbname="agency",
            user=self.login,
            password=self.password,
            host="localhost"
        )) as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """ SELECT *
                        FROM """ + table + """;
                    """
                )
                return cursor.fetchall()

    def showColumnsFromDatabase(self, table="department") :
        with closing(psycopg2.connect(
            dbname="agency",
            user=self.login,
            password=self.password,
            host="localhost"
        )) as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """ SELECT column_name
                    FROM INFORMATION_SCHEMA.COLUMNS
                    WHERE TABLE_NAME = '""" + table + """';
                    """
                )
                result = []
                for row in cursor: result += row

                return result

    def insertToDatabase(self, window) :
        if len(window.table.insertIndexes) is not 0 :
            try :
                data = window.table.data()
                with conn.cursor() as cursor :
                    conn.autocommit = True
                    for i in range(len(window.table.insertIndexes)) :
                        insert = sql.SQL(
                            'INSERT INTO '+ window.table.currentTable +' VALUES {}').format(
                            sql.SQL(',').join(map(sql.Literal, data[i]))
                        )
                        cursor.execute(insert)

            except Exception as ex:
                window.showDialog("Ошибка: " + str(ex))

    def updateToDatabase(self, window) :
        try :
            data = window.table.data()

            headers = [
                window.table.horizontalHeaderItem(i).text()
                for i in range(window.table.columnCount())
            ]

            for i in range(window.table.rowCount()) :
                for j in range(1, window.table.columnCount()) :
                    self.update_vendor(
                        data[i][0],
                        data[i][j],
                        window.table.currentTable,
                        headers
                    )

        except ValueError as ex:
            print("da")
            window.showDialog("Ошибка: " + str(ex))

    def update_vendor(self, id , name, tablename, headers) :
        sql = """
            UPDATE """ + tablename + """
            SET
        """
        for i in range(1, len(headers)) :
            if i is not 0 : sql += ", "
            sql += """ """ + headers[i] + """ = %s """

        sql += """ WHERE """ + headers[0] + """ = %s """
        with closing(psycopg2.connect(
            dbname="agency",
            user=self.login,
            password=self.password,
            host="localhost"
        )) as conn:
            with conn.cursor() as cursor:
                with conn.cursor() as cursor:
                    cursor.execute(sql, (name, id))
                    conn.commit()

    def deleteToDatabase(self, window) :
        if len(window.table.deleteIndexes) is not 0 :
            try :
                data = window.table.data()
                with conn.cursor() as cursor :
                    conn.autocommit = True
                    for i in range(len(window.table.insertIndexes)) :
                        insert = sql.SQL(
                            'DELETE FROM '+ window.table.currentTable +' WHERE id IN ({})').format(
                            sql.SQL(',').join(map(sql.Literal, data[i]))
                        )
                        cursor.execute(insert)

            except Exception as ex:
                window.showDialog("Ошибка: " + str(ex))
