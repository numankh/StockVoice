def userExists(id, cursor):
    cursor.execute("SELECT * FROM master where userId={};".format(id))
    myresult = cursor.fetchall()

    if(len(myresult) == 0):
        print("NEW USER: adding to database")
        return False
    else:
        print("EXISTING USER :)")
        return True

def addUser(conn, cursor, userId, appId, deviceId):
    sql = "INSERT INTO master (userId, appId, deviceId) VALUES (%s, %s, %s)"
    val = (userId, appId, deviceId)
    cursor.execute(sql, val)
    conn.commit()

def addCompany(conn, cursor, userId, company):
    sql = "INSERT INTO company (userId, name) VALUES (%s, %s)"
    val = (userId, company)
    cursor.execute(sql, val)
    conn.commit()