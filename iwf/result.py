from heapq import merge
from unicodedata import category
from .core import *
import json


class Result(object):
    def __init__(self, keywords=[], *args):
        self.keywords = keywords

    def _load_result_page(self, search_url):
        r = requests.get(search_url, headers=HEADERS)
        html = r.text
        return BeautifulSoup(html, "lxml")

    def _scrape_result_info(self, soup_data):
        result = []

        result_container = soup_data.find_all("div", {"class": "result__container"})
        for div_id in result_container:
            if (
                div_id.get("id") == "men_snatchjerk"
                or div_id.get("id") == "women_snatchjerk"
            ):

                cards_container = div_id.find_all("div", {"class": "cards"})
                for cards in cards_container[::3]:
                    card_container = cards.find_all("div", {"class": "card"})

                    for card in card_container[1:]:
                        data_snatch = {}

                        name = card.find_all("p")[1].text.strip()
                        nation = card.find_all("p")[2].text.strip()
                        birthdate = ' '.join(card.find_all("p")[3].text.strip().split()[1:])
                        bodyweight = card.find_all("p")[4].text.strip().split()[1]
                        group = card.find_all("p")[5].text.strip().split()[1]
                        # may need to use use strong tag to get the strike tags
                        # add x if missed lift?
                        snatch1 = card.find_all("p")[6].strong.contents[0]
                        # snatch2 = card.find_all("p")[7].text.strip().split()[1]
                        # snatch3 = card.find_all("p")[8].text.strip().split()[1]
                        # snatch = card.find_all("p")[9].text.strip().split()[1]
                        snatch2 = card.find_all("p")[7].strong.contents[0]
                        snatch3 = card.find_all("p")[8].strong.contents[0]
                        snatch = card.find_all("p")[9].strong.contents[1]

                        
                        category = card.parent.previous_sibling.previous_sibling.previous_sibling.previous_sibling.text.strip()
                        category_number = category.split()[0]
                        gender = category.split()[2]


                        if name and snatch:
                            data_snatch["name"] = name
                            data_snatch["nation"] = nation
                            data_snatch["birthdate"] = birthdate
                            data_snatch["bodyweight"] = bodyweight
                            data_snatch["group"] = group
                            data_snatch["snatch1"] = snatch1
                            data_snatch["snatch2"] = snatch2
                            data_snatch["snatch3"] = snatch3
                            data_snatch["snatch"] = snatch
                            data_snatch["category"] = category_number
                            data_snatch["gender"] = gender
                        result.append(data_snatch)

                for cards in cards_container[1::3]:
                    card_container = cards.find_all("div", {"class": "card"})

                    for card in card_container[1:]:
                        data_cj = {}
                        name = card.find_all("p")[1].text.strip()
                        # print(name)
                        jerk1 = card.find_all("p")[6].strong.contents[0]
                        jerk2 = card.find_all("p")[7].strong.contents[0]
                        jerk3 = card.find_all("p")[8].strong.contents[0]
                        jerk = card.find_all("p")[9].strong.contents[1]

                        if name and jerk:
                            data_cj["name"] = name
                            data_cj["jerk1"] = jerk1
                            data_cj["jerk2"] = jerk2
                            data_cj["jerk3"] = jerk3
                            data_cj["jerk"] = jerk

                        result.append(data_cj)

                for cards in cards_container[2::3]:
                    card_container = cards.find_all("div", {"class": "card"})

                    for card in card_container[1:]:
                        data_total = {}
                        name = card.find_all("p")[1].text.strip()
                        total = card.find_all("p")[8].strong.contents[1]
                        if name and total:
                            data_total["name"] = name
                            data_total["total"] = total
                        result.append(data_total)

        merged_result = {}
        for r in result:
            key = r["name"]
            merged_result.setdefault(key, {}).update(r)

        return list(merged_result.values())

    def get_results(self):
        return
