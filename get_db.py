def getUserDomains(cursor, userId):
    cursor.execute('select name from domain where userId={};'.format(userId))
    myresult = cursor.fetchall()
    
    output = ""
    for x in myresult:
        output = output + x[0] + ","
    output = output[:-1]

    return output

def getUserCompanies(cursor, userId):
    cursor.execute('select name from company where userId={};'.format(userId))
    myresult = cursor.fetchall()
    
    output = ""
    for x in myresult:
        output = output + x[0] + ","
    output = output[:-1]

    return output
