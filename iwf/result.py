from typing import Union
from urllib.parse import urljoin

import requests

from bs4 import BeautifulSoup

from .core import eHeaders, eEvents, eBase


class Result(object):
    def __init__(self):
        pass

    @staticmethod
    def _load_events_page(events_url, old_bw_cat=False) -> BeautifulSoup:
        """Loads the event page for the competition, need to manually specify if it's old weight cats"""
        target_url = urljoin(eBase.URL, eEvents.URL.value + events_url)
        if old_bw_cat:
            target_url = urljoin(eBase.URL, eEvents.OLD_BW_URL.value + events_url)
        r = requests.get(target_url, headers=eHeaders.PAYLOAD)
        html = r.text
        return BeautifulSoup(html, "lxml")

    @staticmethod
    def _scrape_result_info(soup_data):
        """Compiles table data into list[dict] format"""
        result_container = soup_data.find_all("div", {"class": "result__container"})
        if len(result_container) != 0:
            result = []
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
                            birthdate = " ".join(
                                card.find_all("p")[3].text.strip().split()[1:]
                            )
                            bodyweight = card.find_all("p")[4].text.strip().split()[1]
                            group = card.find_all("p")[5].text.strip().split()[1]
                            snatch1 = card.find_all("p")[6].strong.contents[0]
                            snatch2 = card.find_all("p")[7].strong.contents[0]
                            snatch3 = card.find_all("p")[8].strong.contents[0]
                            snatch = card.find_all("p")[9].strong.contents[1]
                            rank_sn = card.find_all("p")[0].text.strip().split()[1]

                            category = (
                                card.parent.previous_sibling.previous_sibling.previous_sibling.previous_sibling.text.strip()
                            )
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
                                data_snatch["rank_sn"] = rank_sn
                                data_snatch["category"] = category_number
                                data_snatch["gender"] = gender
                            result.append(data_snatch)

                    for cards in cards_container[1::3]:
                        card_container = cards.find_all("div", {"class": "card"})

                        for card in card_container[1:]:
                            data_cj = {}
                            name = card.find_all("p")[1].text.strip()
                            jerk1 = card.find_all("p")[6].strong.contents[0]
                            jerk2 = card.find_all("p")[7].strong.contents[0]
                            jerk3 = card.find_all("p")[8].strong.contents[0]
                            jerk = card.find_all("p")[9].strong.contents[1]
                            rank_cj = card.find_all("p")[0].text.strip().split()[1]

                            if name and jerk:
                                data_cj["name"] = name
                                data_cj["jerk1"] = jerk1
                                data_cj["jerk2"] = jerk2
                                data_cj["jerk3"] = jerk3
                                data_cj["jerk"] = jerk
                                data_cj["rank_cj"] = rank_cj

                            result.append(data_cj)

                    for cards in cards_container[2::3]:
                        card_container = cards.find_all("div", {"class": "card"})

                        for card in card_container[1:]:
                            data_total = {}
                            name = card.find_all("p")[1].text.strip()
                            total = card.find_all("p")[8].strong.contents[1]
                            rank = card.find_all("p")[0].text.strip().split()[1]

                            if name and total:
                                data_total["name"] = name
                                data_total["total"] = total
                                data_total["rank"] = rank
                            result.append(data_total)

            merged_result = {}
            for r in result:
                key = r["name"]
                merged_result.setdefault(key, {}).update(r)

            final_table = list(merged_result.values())
            return True, final_table
        return False, []

    def get_results(self, event_url) -> Union[list[dict], False]:
        """Fetches competition data using the result_url"""
        page_data = self._load_events_page(event_url)
        success, data = self._scrape_result_info(page_data)
        if success:
            return data
        elif not success:
            page_data = self._load_events_page(event_url, old_bw_cat=True)
            success, data = self._scrape_result_info(page_data)
            if success:
                return data
        return False
