from .core import *
import json

# from lxml import html
from lxml import etree


class Result(object):
    def __init__(self, keywords=[], *args):
        self.keywords = keywords

    def _load_result_page(self, search_url):
        r = requests.get(search_url, headers=HEADERS)
        html = r.text
        return BeautifulSoup(html, "lxml")

    def _scrape_result_info(self, soup_data):
        result = []

        data = {
            "name": None,  # string
            "birthdate": None,  # string
            "nation": None,  # string
            "athlete_url": None,  # string
            "category": None,  # string
            "bodyweight": None,  # string
            "group": None,  # string
            "snatch1": None,  # string
            "snatch2": None,  # string
            "snatch3": None,  # string
            "snatch": None,  # string
            "jerk1": None,  # string
            "jerk2": None,  # string
            "jerk3": None,  # string
            "jerk": None,  # string
            "total": None,  # string
            "rank_sn": None,  # string
            "rank_cj": None,  # string
            "rank": None,  # string
        }


        for div_id in soup_data.find_all("div", {"class": "result__container"}):
            category = div_id.find_all("div", {'class': 'col-12'})
            print(category)
            
                
            for div_cl in div_id.findAll("div"):

                
                name_container = div_cl.find("div", {"class": "col-7 not__cell__767"})
                if name_container:
                    name = name_container.find("p").string.strip()
                    data["name"] = name
                    data["nation"] = (
                        div_cl.find("div", {"class": "col-3 not__cell__767"})
                        .find("p")
                        .text.strip()
                    )
                
                
                # if category:
                #     data["category"] = category.text.strip()
                    # for res_cont in div_cl.parent.find_all("h2"):
                    #     data["category"] = res_cont.text
                    #     print(res_cont)
                    # print(res_cont)
                    #     # print(sibling)
                    #     print(res_cont.find('div', {'class': 'col-12'}))
                    #     # category = res_cont.find('div', {'class': 'col-12'})
                    #     # if category:
                    #     #     print(category)

                    # print(div_cl.parent.find_all("h2"))

                    # result.append(data)

                    # if div_cl.previous_sibling.find('p') == 'Snatch':
                    #     print('ack')
                    # print(name)
                    # print(name.find('p').text.strip())
                    # if name in data

        return result

        # cards = soup_data.select("div.cards")
        # results = []

        # cards_list = soup_data.find_all('div', {'class': 'cards'})
        # # print(row_list)
        # for card in cards_list:
        #     for car in card.find_all('div', {'class': 'card'}):
        #         data = {
        #             "name": None,  # string
        #             "birthdate": None,  # string
        #             "nation": None,  # string
        #             "athlete_url": None,  # string
        #             "category": None,  # string
        #             "bodyweight": None,  # string
        #             "group": None,  # string
        #             "snatch1": None,  # string
        #             "snatch2": None,  # string
        #             "snatch3": None,  # string
        #             "snatch": None,  # string
        #             "jerk1": None,  # string
        #             "jerk2": None,  # string
        #             "jerk3": None,  # string
        #             "jerk": None,  # string
        #             "total": None,  # string
        #             "rank_sn": None,  # string
        #             "rank_cj": None,  # string
        #             "rank": None,  # string
        #         }
        #         # print(car)
        #         name = car.find("div", {"class": "col-7 not__cell__767"})
        #         # print(name)
        #         if name and name != None:
        #             # print(name)
        #             data["name"] = name.find('p').text.strip()
        #         # name = car.find("div", {"class": "col-7 not__cell__767"}).find('p').text.strip()
        #         # if name:
        #         #     data["name"] = name
        #         # print(name)
        #         # print(car)

        #     results.append(data)

        # return results

    def get_results(self):
        return
