import requests
from set_url import SetURL
from set_url import categrory_list
import pygal
from pygal import Config
from pygal.style import LightColorizedStyle
from countries import Country_ISO_CODE



# how many news are we interested in
PAGE_SIZE = 10
PAGE_SIZE_UPDATE = PAGE_SIZE
# country for the search options
country_code = Country_ISO_CODE.USA.value

# Creating the instance of a class to manage url requests
url = SetURL()

# a comprehensive dictionary of all news for each category
dict_news_all = {}


# if the reading news was sucesful , draw the graph
reading_news_sucess = False 

for category_news in categrory_list : 

    # reading the feeds from news API for the given search option
    url_r = url.return_url_headlines(category=category_news,\
        country=country_code,pageSize=PAGE_SIZE,page=1)

    # getting the response from the news API and storing it in a dict
    response = requests.get(url_r)
    response_dict = response.json()

    # print(response_dict)

    # checking if the request was sucesful
    if response_dict['status'].lower() == 'ok':

        # Creating an empty list of dictioray for current news
        news_list_dict = []

        # Creating lists of titles and urls of the news
        list_titles = [dict_news[keys] for articles in response_dict \
            if 'articles' in articles for dict_news in response_dict[articles] \
                for keys in dict_news if keys == 'title' ]
        list_urls = [dict_news[keys] for articles in response_dict \
            if 'articles' in articles for dict_news in response_dict[articles] \
                for keys in dict_news if keys == 'url' ]
        # Creating list of values for dot chart in pygal
        list_values = [1 for i in range(PAGE_SIZE)]

        # creating specific dictionary of each news, and checkign if size is bigger
        # than the actual found results
        PAGE_SIZE_UPDATE = min(PAGE_SIZE,response_dict['totalResults'])
        for value in range(PAGE_SIZE_UPDATE):
            current_news_dict = {
                'label' : list_titles[value],
                'value' : list_values[value],
                'xlink' : list_urls[value]
            }
            # creating a lsit of dictionaries / news
            news_list_dict.append(current_news_dict)


        # key is our cathegory , and values are all the news
        dict_news_all[category_news] = news_list_dict
        reading_news_sucess = True
        print("{} Reading news sucesful".format(category_news))

    # error occured during last call
    else:
        print("Error")
        print(response_dict['status'] +" - "+ response_dict['code'] + " - " + \
            response_dict['message'])
        reading_news_sucess = False


if reading_news_sucess:
    # configuration of the chart
    my_style = LightColorizedStyle()
    my_style.tooltip_font_size = 7
    config_chart = Config()
    config_chart.x_label_rotation = 30
    config_chart.title = 'TOP HEADLINES'
    config_chart.tooltip_fancy_mode = False

    dot_chart = pygal.Dot(config_chart,style=my_style)
    # The number of news
    dot_chart.x_labels = [x for x in range(1,PAGE_SIZE_UPDATE+1)]

    # addin all the categories to the chart
    for nmber in range(len(categrory_list)):
        dot_chart.add(categrory_list[nmber],dict_news_all[categrory_list[nmber]])
    # drawing the news into the chart
    dot_chart.render_to_file("News_API\\data\\NEWS_HEADLINES.svg")
    print("Writing graph sucesful")

else : 
    print("ERROR")
    print("Reading news unsuccessful")

