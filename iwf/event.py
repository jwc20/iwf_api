from hashlib import new
from unittest import result

from .core import *
import json

# TODO: add method for combining year and other filters


class Event(object):
    def __init__(self, keywords=[], *args):
        self.keywords = keywords

    # def _craft_bodyweight_url(self, new_or_old):
    #     if new_or_old == "old":
    #         return BASE_URL + OLD_BW_EVENTS_URL
    #     # if new_or_old == "new":
    #     else:
    #         return BASE_URL + EVENTS_URL

    def _craft_url(
        self,
        new_or_old=None,
        year=None,
        nation=None,
        event_type=None,
        age_group=None,
    ):
        search_url = ""
        filters = []
        # if url and is_event(url):
        #     r = requests.get(url, headers=HEADERS)

        # print(new_or_old)
        # if new_or_old:
        #     # this is for 2018
        #     search_url = self._craft_bodyweight_url(new_or_old)
        if new_or_old == "old":
            search_url = BASE_URL + OLD_BW_EVENTS_URL
        else:
            search_url = BASE_URL + EVENTS_URL

        if year:
            search_url += YEAR_URL + year
        else:
            if event_type:
                if " " in event_type:
                    event_type_new = event_type.replace(" ", "+")
                    filters.append(EVENT_TYPE_URL + event_type_new)
            if age_group:
                filters.append(EVENT_AGE_URL + age_group)
            if nation:
                filters.append(EVENT_NATION_URL + nation)

        if len(filters) >= 1:
            search_url += "/?" + filters[0]
            for i in range(1, len(filters)):
                search_url += "&" + filters[i]
        return search_url

    def _load_event_page(
        self,
        search_url=None,
        new_or_old=None,
        year=None,
        nation=None,
        event_type=None,
        age_group=None,
    ):

        if search_url and is_event(search_url):
            r = requests.get(search_url, headers=HEADERS)
        else:
            # print(new_or_old)
            new_url = self._craft_url(
                new_or_old,
                year,
                nation,
                event_type,
                age_group,
            )
            r = requests.get(new_url, headers=HEADERS)

        html = r.text
        return BeautifulSoup(html, "lxml")

    # def _scrape_event_type(self):
    #     return

    # def _scrape_event_age_group(self):
    #     return

    # def _scrape_event_nation(self):
    #     return

    # TODO Don't really need this
    # def _scrape_a_event(self, soup_data):
    #     # print(soup_data.findAll("a", {"class": "card"}))
    #     return soup_data.findAll("a", {"class": "card"})



    def _scrape_event_info(self, soup_data): 
        result = []
        data = {
            "name": None,  # string
            "result_url": None,  # string
            "location": None,  # string
            "date": None,  # string
        }

        
        cards = soup_data.findAll("a", {"class": "card"})

        # cards = self._scrape_a_event(soup_data)
        
        # print(cards[0])
        for i, card in enumerate(cards):
            # print('result: ', result)
            
            # data = EventInfo()
            # print("##############################################",card)
            # data["name"] = card.find("span", {"class": "text"}).string
            data["name"] = card.xpath("//div[2]/a[1]/div[1]/div/div[1]/p/span")
            # data["result_url"] = card["href"]
            # # print(card['href'])
            # data["location"] = card.find("strong").string
            # data["date"] = card.find("p", {"class": "normal__text"}).string.strip()
            # print(card.find("p", {"class": "normal__text"}).string.strip())
            # print(data)
            result.append(data)
        print(result)
            
            

        # print(result)
        # return json.dumps(result)

        # data["name"] = soup_data.find("span").find("text")
        # print()

        return result

    def get_events(
        self,
        year=None,
        search_url=None,
        new_or_old=None,
        nation=None,
        event_type=None,
        age_group=None,
    ):
        # bodyweight=None,
        # quantity=None,
        # infinity=False,
        # sort_by=None,

        # for event in self._scrape_a_event(
        #     self._load_event_page(
        #         search_url,
        #         new_or_old,
        #         year,
        #         nation,
        #         event_type,
        #         age_group,
        #     )
        # ):
        result_data = self._scrape_event_info(self._load_event_page(search_url, new_or_old, year, nation, event_type, age_group))
        # print(result_data)
        if result_data:
          return result_data
            # if data_dict:
            #     yield data_dict
            # print(data_dict)
        # return data_dict


# class EventInfo:
#     def __init__(self, args=None):
#         self.name = ''
#         self.location = ''
#         self.result_url = ''
#         self.nation = ''
