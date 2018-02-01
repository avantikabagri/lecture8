#ny-simple.py

import secrets
import requests
import json


# gets stories from a particular section of NY times

def get_stories(section):

    baseurl = 'https://api.nytimes.com/svc/topstories/v2/'
    extendedurl = baseurl + section + '.json'
    params={'api-key': secrets.nyt_key}
    return requests.get(extendedurl, params).json()

section = 'science'
stories = get_stories(section)
print(stories) # should print a big pile of json

def get_headlines(nyt_results_dict):
    results = nyt_results_dict['results']
    headlines = []
    for r in results:
        headlines.append(r['title'])
    return headlines


story_list_json = get_stories('science')
headlines = get_headlines(story_list_json)
for h in headlines:
    print(h)
