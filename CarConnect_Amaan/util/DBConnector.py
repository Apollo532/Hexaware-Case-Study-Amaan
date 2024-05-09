import mysql.connector as sql

class DBConnector:
    @staticmethod
    def openConnection():
        try:
            conn = sql.connect(host='localhost', database='Car', user='root', password='Amaan123')
            return conn
        except Exception as e:
            print(str(e) + "  Couldn't connect to CarConnect Database:")

    @staticmethod
    def closeConnection(conn, cs):
        cs.close()
        conn.close()
        print("Connection to CarConnect Database Closed")