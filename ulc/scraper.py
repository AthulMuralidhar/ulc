"""
- scrap open source projects for python and js code
- compile them into a csv and make a dump

ref: natural language processing with python
"""
import requests
from bs4 import BeautifulSoup


def scraper(source):
    # get a list of projects to scrap from form the sources
    
    # import ipdb; ipdb.set_trace();

    PROJECT_URL_LIST = []
    for s in source:
        r_get = requests.get(s)
        # print(r_get.text)

        soup = BeautifulSoup(r_get.text, 'html.parser')

        # print(soup)

        print(soup.find_all("a", {"data-ga-click":"Explore, go to repository, location:explore feed"}))
        # not working correctly returning a [] now for some reason
        # need to find a class that will get me to the above <a> with that text in  data-ga-click 
        # attribute
        print(len(soup.find_all("a", {"data-ga-click":"Explore, go to repository, location:explore feed"})))

        """
        next steps
        - there are 70 entities in the list above
            - i do not think that all the 70 <a>'s have valid urls
        - so make a get again to the url and then pic a random set of numbers
            - while writing this, i realise that it is maybe much easier to clone
            the repo locally and then run a dataprocessor to parse through the repo and then
            just build a dump then use that for the transformer vocabulary
        """
        break

    

if __name__ == "__main__":
    SCRAPING_SOURCES = {
        "github-javascript": "https://github.com/topics/javascript",
        "github-go": "https://github.com/topics/go"
    }

    scraper([SCRAPING_SOURCES[key] for key in SCRAPING_SOURCES.keys()])
