import mysql.connector

def query_in(inq):
    try:

        conn = mysql.connector.connect(host="localhost", user='root', password='vasiliy6667', database='database2')
        cur = conn.cursor()
        cur.execute(inq)
        results = cur.fetchall()
        cur.close()
        conn.close()
        return results
    except:
        pass


def query_ins(inq):
    try:
        conn = mysql.connector.connect(host="localhost", user='root', password='vasiliy6667', database='database2')
        cur = conn.cursor()
        cur.execute(inq)
        conn.commit()
        cur.close()
        conn.close()
    except:
        pass