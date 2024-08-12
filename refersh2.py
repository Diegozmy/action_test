import mysql.connector
from requests import get

# 连接到MySQL数据库

cnx = mysql.connector.connect(user='husky',
                              password='Zmy@20090622',
                              port=60554,
                              host='frp-end.top',
                              database='my_database')
cursor = cnx.cursor()

cursor.execute("SELECT * FROM urls")
urls=[row[1] for row in cursor.fetchall()]
for url in urls:
    print(url)
    try:
        re = get(f"http://{url}/go.js")
        go_url = re.text.split("'")[1]
        print(go_url)
        re = get(go_url)
        re.encoding = "utf-8"
        new = re.text.split('<script type="text/javascript">document.write(secdotxts+".")</script>')[-1].split("</h1>")[
            0]
        print(new)
        if new not in urls:
            sql = "INSERT INTO urls (url) VALUES (%s)"
            val = (new,)
            cursor.execute(sql, val)
            cnx.commit()
        else:
            print("same")
        break
    except:
        sql = f"DELETE FROM urls WHERE url = '{url}';"
        cursor.execute(sql)
        cnx.commit()
        continue


cursor.close()
cnx.close()
