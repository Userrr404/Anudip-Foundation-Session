import mysql.connector

def get_connection():
    db = mysql.connector.connect(
    host="localhost",
    port=3310,
    user="root",
    passwd="TRxGalaxyBoyy"
)

    cur = db.cursor()

    cur.execute("CREATE DATABASE IF NOT EXISTS DB_Banking")

    cur.execute("USE DB_Banking")

    cur.execute(
        "CREATE TABLE IF NOT EXISTS accounts(account_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), balance DECIMAL(10,2))"
    )

    # cur.execute("INSERT INTO accounts (name, balance) VALUES (%s, %s)", ("Yogesh Lilake",20000.00))

    # # commit the change
    # db.commit()

    cur.close()

    db.close()

    return mysql.connector.connect(
        host="localhost",
        port=3310,
        user="root",
        passwd="TRxGalaxyBoyy",
        database="DB_Banking"
    )

