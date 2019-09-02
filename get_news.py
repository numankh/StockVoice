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

def getUserCompanies(cursor, userId):
    cursor.execute('select name from company where userId={};'.format(userId))
    myresult = cursor.fetchall()
    
    output = ""
    for x in myresult:
        output = output + x[0] + ","
    output = output[:-1]

    return output

def getPortfolioNews(cursor, userId):
    newsapi = NewsApiClient(api_key=os.getenv('newsApiKey'))
    userDomains = getUserDomains(cursor, userId)
    userCompanies = getUserCompanies(cursor, userId)
    output = ""
    userCompanies = userCompanies.split(',')
    
    for companyName in userCompanies:
        all_articles = newsapi.get_everything(q=companyName,
                                              sources=userDomains,
                                              language='en',
                                              sort_by='relevancy',
                                              page=1)
                                      
        count = 1
        if(len(all_articles) != 0):
            for x in all_articles['articles']:
                if(count == 2):
                    break
                output = output + companyName +" Article: " + x['title'] + ", "
                count += 1
    return output[:-2]