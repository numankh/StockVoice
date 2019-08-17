from newsapi import NewsApiClient
import config

newsapi = NewsApiClient(api_key=config.api_key)

apple_articles = newsapi.get_everything(q='apple',
                                      from_param='2019-08-10',
                                      to='2019-08-16',
                                      language='en',
                                      sort_by='relevancy')
                    
print(apple_articles)