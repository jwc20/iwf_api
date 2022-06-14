from heapq import merge
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

            # id="men_total"
            # men_snatchjerk
            # women_total
            # women_snatchjerk

            if (
                div_id.get("id") == "men_snatchjerk"
                or div_id.get("id") == "women_snatchjerk"
            ):

                cards_container = div_id.find_all("div", {"class": "cards"})
                data = {}

                # getting the names, nation, birthdate, bodyweight, group, and snatches
                for cards in cards_container[::3]:
                    card_container = cards.find_all("div", {"class": "card"})

                    for card in card_container[1:]:
                        # data = {
                        #     "name": None,  # string
                        #     "birthdate": None,  # string
                        #     "nation": None,  # string
                        #     "athlete_url": None,  # string
                        #     "category": None,  # string
                        #     "bodyweight": None,  # string
                        #     "group": None,  # string
                        #     "snatch1": None,  # string
                        #     "snatch2": None,  # string
                        #     "snatch3": None,  # string
                        #     "snatch": None,  # string
                        #     "jerk1": None,  # string
                        #     "jerk2": None,  # string
                        #     "jerk3": None,  # string
                        #     "jerk": None,  # string
                        #     "total": None,  # string
                        #     "rank_sn": None,  # string
                        #     "rank_cj": None,  # string
                        #     "rank": None,  # string
                        # }

                        data_snatch = {}

                        name = card.find_all("p")[1].text.strip()
                        nation = card.find_all("p")[2].text.strip()
                        birthdate = card.find_all("p")[3].text.strip()
                        bodyweight = card.find_all("p")[4].text.strip()
                        group = card.find_all("p")[5].text.strip()
                        # may need to use use strong tag to get the strike tags
                        # add x if missed lift?
                        snatch1 = card.find_all("p")[6].strong
                        snatch2 = card.find_all("p")[7].text.strip().split()[1]
                        snatch3 = card.find_all("p")[8].text.strip().split()[1]
                        snatch = card.find_all("p")[9].text.strip().split()[1]

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
                            data_snatch[
                                "category"
                            ] = (
                                card.parent.previous_sibling.previous_sibling.previous_sibling.previous_sibling.text.strip()
                            )
                        result.append(data_snatch)

                for cards in cards_container[1::3]:
                    card_container = cards.find_all("div", {"class": "card"})

                    for card in card_container[1:]:
                        data_cj = {}
                        name = card.find_all("p")[1].text.strip()
                        # print(name)
                        jerk1 = card.find_all("p")[6].text.strip()
                        jerk2 = card.find_all("p")[7].text.strip()
                        jerk3 = card.find_all("p")[8].text.strip()
                        jerk = card.find_all("p")[9].text.strip()

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
                        total = card.find_all("p")[8].text.strip()
                        if name and total:
                            data_total["name"] = name
                            data_total["total"] = total
                        result.append(data_total)
        
        merged_result = {}
        for r in result:
            key = r["name"]
            merged_result.setdefault(key, {}).update(r)

        return list(merged_result.values())

        # return result

    def get_results(self):
        return
