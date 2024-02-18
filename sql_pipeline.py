import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='chiOS101418',
    db='collatz',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor,
)

