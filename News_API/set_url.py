from dotenv import dotenv_values
from enum import Enum

class Endpoint(Enum):
    """storing endpoint options for the 3 main api requests"""

    ENDPOINT_EVERYTHING = 'everything'
    ENDPOINT_TOP_HEADLINES = 'top-headlines'
    ENDPOINT_SOURCES = 'sources'

# list of possible categories business entertainment general health science 
# sports technology
categrory_list = ['business','entertainment','general','health','science',\
    'sports','technology']


class SetURL():
    """Creating and managing the url for get request"""

    def __init__(self) -> None:
        
        # Reading the env variables - API - KEY
        self.ENV_VAR = dotenv_values()
        self.base_url = "https://newsapi.org/v2/"

    def return_url_everything(self, keyword : str, searchin : str = None, \
        from_time : str = None , to_time : str = None, language : str = None, \
            sortBy : str = None, pageSize : int = None, \
                page : int = None) -> str :
        """returning the url as a string for the request"""
        """managing all the options reagrding top-headlines endpoint"""
        """Search through millions of articles from over 80,000 large and small 
        news sources and blogs. This endpoint suits article discovery and 
        analysis."""

        # Creating the base of the URL
        # "https://newsapi.org/v2/everything?"
        self.url = self.__return_endpoint_url(Endpoint.ENDPOINT_EVERYTHING.value)
        
        
        # Keywords or phrases to search for in the article title and body.
        # Advanced search is supported here:
        # Surround phrases with quotes (") for exact match.
        # Prepend words or phrases that must appear with a + symbol. Eg: +bitcoin
        # Prepend words that must not appear with a - symbol. Eg: -bitcoin
        # Alternatively you can use the AND / OR / NOT keywords, and optionally 
        # group these with parenthesis. Eg: crypto AND (ethereum OR litecoin) 
        # NOT bitcoin.
        # The complete value for q must be URL-encoded. Max length: 500 chars.     
        if keyword:
            self.url += 'q=' + str(keyword) + '&'
        
        # The fields to restrict your q (keywords) search to
        # Default: all fields are searched
        if searchin:
            # only three options posible 
            if 'title' in searchin or 'description' in searchin or 'content' in searchin:
                self.url += 'searchIn=' + str(searchin) + '&'

        # A date and optional time for the oldest article allowed. 
        # This should be in ISO 8601 format (e.g. 2022-05-04 or 
        # 2022-05-04T21:41:18)
        # Default: the oldest according to your plan.
        if from_time:
            self.url += 'from=' + str(from_time) + '&'

        # A date and optional time for the newest article allowed. 
        # This should be in ISO 8601 format (e.g. 2022-05-04 or
        # 2022-05-04T21:41:18)
        # Default: the newest according to your plan.
        if to_time: 
            self.url += 'to=' + str(to_time) + '&'

        # The 2-letter ISO-639-1 code of the language you want to get 
        # headlines for. Possible options: ar de en es fr he it nl no pt ru sv 
        # ud zh.
        # Default: all languages returned.
        if language:
            self.url += 'language=' + str(language) + '&'


        # The order to sort the articles in. Possible options: relevancy, 
        # popularity, publishedAt.
        # relevancy = articles more closely related to q come first.
        # popularity = articles from popular sources and publishers come first.
        # publishedAt = newest articles come first.
        # Default: publishedAt
        if sortBy:
            self.url += 'sortBy=' + str(sortBy) + '&'

        # The number of results to return per page.
        # Default: 100. Maximum: 100
        if pageSize:
            self.url += 'pageSize=' + str(pageSize) + '&'

        # Use this to page through the results.
        # Default: 1
        if page:
            self.url += 'page=' + str(page) + '&'


        # +'apiKey=API_KEY'
        return self.__addin_API_KEY(self.url) 
    

    def return_url_headlines(self, country : str = None, category : str = None,\
         sources : str = None, q : str = None, pageSize : int = None, \
                page : int = None) -> str :
        """returning the url as a string for the request"""
        """managing all the options reagrding sources endpoint"""
        """This endpoint provides live top and breaking headlines for a country,
         specific category in a country, single source, or multiple sources. 
         You can also search with keywords. Articles are sorted by the earliest 
         date published first.This endpoint is great for retrieving headlines 
         for use with news tickers or similar."""

        # Creating the base of the URL
        # "https://newsapi.org/v2/top-headlines?"
        self.url = self.__return_endpoint_url(Endpoint.ENDPOINT_TOP_HEADLINES.value)
        

        # The 2-letter ISO 3166-1 code of the country you want to get headlines 
        # for. Possible options: 
        # ae ar at au be bg br ca ch cn co cu cz de eg fr gb gr hk hu id ie il 
        # in it jp kr lt lv ma mx my ng nl no nz ph pl pt ro rs ru sa se sg si 
        # sk th tr tw ua us ve za. 
        # Note: you can't mix this param with the sources param.
        if country and sources == None:
            self.url += 'country=' + str(country) + '&'


        # The category you want to get headlines for. Possible options: 
        # business, entertainment, general, health, science, sports, technology. 
        # Note: you can't mix this param with the sources param.
        if category and sources == None:
            self.url += 'category=' + str(category) + '&'

        # A comma-seperated string of identifiers for the news sources or 
        # blogs you want headlines from. Use the /top-headlines/sources 
        # endpoint to locate these programmatically or look at the sources
        # index. Note: you can't mix this param with the country or category 
        # params.
        if sources and country == None and category == None:
            self.url += 'sources=' + str(sources) + '&'

        # Keywords or a phrase to search for.
        if q :
            self.url += 'q=' + str(q) + '&'


        # The number of results to return per page (request). 20 is the default,
        # 100 is the maximum
        if pageSize:
            self.url += 'pageSize=' + str(pageSize) + '&'

        # Use this to page through the results if the total results found is 
        # greater than the page size.
        if page:
            self.url += 'page=' + str(page) + '&'

        # +'apiKey=API_KEY'
        return self.__addin_API_KEY(self.url) 
        

    def return_url_source(self, category : str = None, language : str = None, \
        country : str = None) -> str :
        """returning the url as a string for the request"""
        """managing all the options reagrding everything endpoint"""
        """This endpoint returns the subset of news publishers that top 
        headlines (/v2/top-headlines) are available from. It's mainly
        a convenience endpoint that you can use to keep track of the publishers 
        available on the API, and you can pipe it straight through to your 
        users."""


        # Creating the base of the URL
        # "https://newsapi.org/v2/top-headlines/sources?"
        self.url = self.__return_endpoint_url(Endpoint.ENDPOINT_SOURCES.value)


        # Find sources that display news of this category. Possible options: 
        # business entertainment general health science sports technology. 
        # Default: all categories.
        if category:
            self.url += 'category=' + str(category) + '&'

        # Find sources that display news in a specific language. Possible 
        # options: ardeenesfrheitnlnoptrusvudzh.
        # Default: all languages.
        if language:
            self.url += 'language=' + str(language) + '&'

        # Find sources that display news in a specific country. Possible options: 
        # ae ar at au be bg br ca ch cn co cu cz de eg fr gb gr hk hu id ie il 
        # in it jp kr lt lv ma mx my ng nl no nz ph pl pt ro rs ru sa se sg si 
        # sk th tr tw ua us ve za. 
        # Default: all countries.
        if country:
            self.url += 'country=' + str(country) + '&'

        # +'apiKey=API_KEY'
        return self.__addin_API_KEY(self.url) 
        
        

    def __addin_API_KEY(self, url : str ) -> str:
        """Adding API_KEY to the URL """
        return url + 'apiKey=' + self.ENV_VAR['API_KEY']

    def __return_endpoint_url(self, endpoint : str = 'everything') \
        -> str:
        """returning the endpoint url as a string"""
        """endpoint -> three options : everything, top-headlines, sources"""

        # 3 options for a endpoint 
        self.endpoit_option = ''
        # search every article published by over 80,000 different sources
        # large and small in the last 4 years. This endpoint is ideal for news 
        # analysis and article discovery
        if endpoint == 'everything':
            self.endpoit_option = 'everything?'

        # This endpoint provides live top and breaking headlines for a country, 
        # specific category in a country, single source, or multiple sources. 
        # You can also search with keywords. Articles are sorted by the earliest
        #  date published first. This endpoint is great for retrieving headlines 
        # for use with news tickers or similar.
        elif endpoint == 'top-headlines':
            self.endpoit_option = 'top-headlines?'

        # This endpoint returns the subset of news publishers that top headlines 
        # (/v2/top-headlines) are available from. It's mainly a convenience 
        # endpoint that you can use to keep track of the publishers available
        #  on the API, and you can pipe it straight through to your users.
        elif endpoint == 'sources':
            self.endpoit_option = 'top-headlines/sources?'

        # adding the api key at the end
        return self.base_url + self.endpoit_option
