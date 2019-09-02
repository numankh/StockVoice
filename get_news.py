from newsapi import NewsApiClient
import os

def getCompanyNews(cursor, userId, companyName):
    userDomains = getUserDomains(cursor, userId)
    newsapi = NewsApiClient(api_key=os.getenv('newsApiKey'))

    all_articles = newsapi.get_everything(q=companyName,
                                      sources=userDomains,
                                      language='en',
                                      sort_by='relevancy')
                                      
    count = 1
    output = ""
    if(len(all_articles) != 0):
        for x in all_articles['articles']:
            if(count == 4):
                break
            output = output + "Article " + str(count) + ": " + x['title'] + ", "
            count += 1
    return output[:-2]

def getUserDomains(cursor, userId):
    cursor.execute('select name from domain where userId={};'.format(userId))
    myresult = cursor.fetchall()
    
    output = ""
    for x in myresult:
        output = output + x[0] + ","
    output = output[:-1]

    return output
