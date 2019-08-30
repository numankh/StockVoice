def userExists(id, cursor):
    cursor.execute("SELECT * FROM master where userId={}".format(id))
    myresult = cursor.fetchall()

    if(len(myresult) == 0):
        print("NEW USER: adding to database")
        addUser(id, cursor)
    else:
        print("EXISTING USER :)")

def addUser(id, cursor):
    sql = "INSERT INTO master (userId, appId, deviceId) VALUES (%s, %s, %s)"
    val = (id, "blah", "blah")
    cursor.execute(sql, val)
