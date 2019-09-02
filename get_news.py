from newsapi import NewsApiClient
import get_db
import os

def getCompanyNews(cursor, userId, companyName):
    userDomains = get_db.getUserDomains(cursor, userId)
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

def getPortfolioNews(cursor, userId):
    newsapi = NewsApiClient(api_key=os.getenv('newsApiKey'))
    userDomains = get_db.getUserDomains(cursor, userId)
    userCompanies = get_db.getUserCompanies(cursor, userId)
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