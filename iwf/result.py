from .core import *
import json
import re

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

        result_container = soup_data.find_all("div", {"class": "result__container"})
        for div_id in result_container:

            # id="men_total"
            # men_snatchjerk
            # women_total
            # women_snatchjerk

            # print(len(result_container))
            # print(div_id if div_id.get("id") == "men_snatchjerk" else "ACK")

            if (
                div_id.get("id") == "men_snatchjerk"
                or div_id.get("id") == "women_snatchjerk"
            ):

                category = div_id.find_all("div", {"class": "col-12"})

                # data["name"] = (
                #     div_id.find("div", {"class": "col-7 not__cell__767"})
                #     .find("p")
                #     .text.strip()
                # )


                cards_container = div_id.find_all("div", {"class": "cards"})

                # getting the names, nation, birthdate, bodyweight, group, and snatches
                for cards in cards_container[::3]:
                    card_container = cards.find_all("div", {"class": "card"})

                    for card in card_container[1:]:

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
                        name = card.find_all("p")[1].text.strip()
                        nation = card.find_all("p")[2].text.strip()
                        birthdate = card.find_all("p")[3].text.strip()
                        bodyweight = card.find_all("p")[4].text.strip()
                        group = card.find_all("p")[5].text.strip()
                        snatch1 = card.find_all("p")[6].text.strip().split()[1]
                        snatch2 = card.find_all("p")[7].text.strip().split()[1]
                        snatch3 = card.find_all("p")[8].text.strip().split()[1]
                        snatch = card.find_all("p")[9].text.strip().split()[1]

                        if name and snatch:

                            data["name"] = name
                            data["nation"] = nation
                            data["birthdate"] = birthdate
                            data["bodyweight"] = bodyweight
                            data["group"] = group
                            data["snatch1"] = snatch1
                            data["snatch2"] = snatch2
                            data["snatch3"] = snatch3
                            data["snatch"] = snatch
                            data[
                                "category"
                            ] = (
                                card.parent.previous_sibling.previous_sibling.previous_sibling.previous_sibling.text.strip()
                            )

                        result.append(data)

        return result

    def get_results(self):
        return
