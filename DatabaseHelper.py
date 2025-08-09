import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Thisisastrongpassword',
    port='3306',
    database='kids_learning'
)

myCursor = mydb.cursor()
loginValidation = None
levelV = ""

def insertAccount(username, password, displayAccountValidity, successFullInsert):
    # Check if the username already exists
    check_query = "SELECT * FROM users WHERE username = %s"
    myCursor.execute(check_query, (username,))
    existing_user = myCursor.fetchone()

    if existing_user:
        print("Username already exists. Please choose a different username.")
        displayAccountValidity(3)
    else:
        insert_query = "INSERT INTO users (username, password, level) VALUES (%s, %s, %s)"
        myCursor.execute(insert_query, (username, password, 1))
        mydb.commit()
        print("Successfully Insert " + username + " " + password)
        successFullInsert(3)


def getUsernameAndPassword(username, password):
    global loginValidation

    sql = "SELECT * FROM users WHERE username = %s and password = %s"
    myCursor.execute(sql, (username, password))
    results = myCursor.fetchall()

    if results:
        loginValidation = True
    else:
        loginValidation = False

    return loginValidation

def getLevel(username):
    query = "SELECT level FROM users WHERE username = %s"
    myCursor.execute(query, (username,))
    result = myCursor.fetchone()

    if result:
        levelV = result[0]
        return levelV
    else:
        return None

def updateLevel(username, level):
    query = "UPDATE users SET level = %s WHERE username = %s"
    values = (level, username)

    myCursor.execute(query, values)
    mydb.commit()