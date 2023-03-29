from typing import Union
from urllib.parse import urljoin

import requests
import time
import logging
from bs4 import BeautifulSoup

from .core import eHeaders, eEvents, eBase

import re

from pprintpp import pprint


def update_rank_sn_by_category(final_table):
    # Group the final table by category
    categories = {}
    for entry in final_table:
        category = entry["category"]
        if category not in categories:
            categories[category] = []
        categories[category].append(entry)

    # Sort each category based on snatch values and bodyweight, considering only valid entries
    for category, athletes in categories.items():
        sorted_athletes = sorted(
            [entry for entry in athletes if entry["snatch"] != "---"],
            key=lambda x: (float(x["snatch"]), float(x["bodyweight"])),
            reverse=True,
        )

        # Update the rank_sn values based on the sorted list for each category
        for index, entry in enumerate(sorted_athletes, start=1):
            entry["rank_sn"] = str(index)

        # Update the original final_table with the new rank_sn values
        for sorted_entry in sorted_athletes:
            for original_entry in final_table:
                if sorted_entry["name"] == original_entry["name"]:
                    original_entry["rank_sn"] = sorted_entry["rank_sn"]
                    break

    return final_table


def update_rank_cj_by_category(final_table):
    # Group the final table by category
    categories = {}
    for entry in final_table:
        category = entry["category"]
        if category not in categories:
            categories[category] = []
        categories[category].append(entry)

    # Sort each category based on clean & jerk values and bodyweight, considering only valid entries
    for category, athletes in categories.items():
        sorted_athletes = sorted(
            [entry for entry in athletes if entry["jerk"] != "---"],
            key=lambda x: (float(x["jerk"]), float(x["bodyweight"])),
            reverse=True,
        )

        # Update the rank_cj values based on the sorted list for each category
        for index, entry in enumerate(sorted_athletes, start=1):
            entry["rank_cj"] = str(index)

        # Update the original final_table with the new rank_cj values
        for sorted_entry in sorted_athletes:
            for original_entry in final_table:
                if sorted_entry["name"] == original_entry["name"]:
                    original_entry["rank_cj"] = sorted_entry["rank_cj"]
                    break
    return final_table


class Result(object):
    def __init__(self):
        pass

    @staticmethod
    def _load_events_page(events_url, old_bw_cat=False) -> BeautifulSoup:
        """Loads the event page for the competition, need to manually specify if it's old weight cats"""

        # Build url
        target_url = urljoin(eBase.URL, eEvents.URL.value + events_url)
        if old_bw_cat:
            target_url = urljoin(eBase.URL, eEvents.OLD_BW_URL.value + events_url)

        MAX_RETRIES = 10

        logging.basicConfig(filename="scraper.log", level=logging.ERROR)

        for i in range(MAX_RETRIES):
            try:
                r = requests.get(target_url, headers=eHeaders.PAYLOAD)
                break

            except requests.Timeout:
                print(
                    f"Timeout error: Request to {url} timed out after {timeout} seconds."
                )

            except requests.HTTPError as e:
                print(f"HTTP error occurred: {e}")

            except requests.exceptions.RequestException as e:
                print(
                    f"An error occurred while fetching data: {e}, attempt number: ", i
                )
                if i == MAX_RETRIES - 1:
                    logging.error(f"Error occurred: {e}")

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

                            if len(card.find_all("p")[5].text.strip().split()) < 2:
                                group = ""
                            else:
                                group = card.find_all("p")[5].text.strip().split()[1]

                            snatch1_tag = card.find_all("p")[6].strong.contents[0]
                            snatch1 = (
                                snatch1_tag
                                if isinstance(snatch1_tag, str)
                                else str(snatch1_tag)
                            )

                            snatch2_tag = card.find_all("p")[7].strong.contents[0]
                            snatch2 = (
                                snatch2_tag
                                if isinstance(snatch2_tag, str)
                                else str(snatch2_tag)
                            )

                            snatch3_tag = card.find_all("p")[8].strong.contents[0]
                            snatch3 = (
                                snatch3_tag
                                if isinstance(snatch3_tag, str)
                                else str(snatch3_tag)
                            )

                            snatch = card.find_all("p")[9].strong.contents[1]

                            if len(card.find_all("p")[0].text.strip().split()) < 2:
                                rank_sn = ""
                            else:
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
                            jerk1_tag = card.find_all("p")[6].strong.contents[0]
                            jerk1 = (
                                jerk1_tag
                                if isinstance(jerk1_tag, str)
                                else str(jerk1_tag)
                            )

                            jerk2_tag = card.find_all("p")[7].strong.contents[0]
                            jerk2 = (
                                jerk2_tag
                                if isinstance(jerk2_tag, str)
                                else str(jerk2_tag)
                            )

                            jerk3_tag = card.find_all("p")[8].strong.contents[0]
                            jerk3 = (
                                jerk3_tag
                                if isinstance(jerk3_tag, str)
                                else str(jerk3_tag)
                            )

                            jerk = card.find_all("p")[9].strong.contents[1]

                            if len(card.find_all("p")[0].text.strip().split()) < 2:
                                rank_cj = ""
                            else:
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

            for data in final_table:
                full_name = data["name"]
                words = full_name.split()
                for i, word in enumerate(words):
                    if i == 0:
                        last_name = word
                    elif word[0].isupper() and not word.isupper():
                        first_name = " ".join(words[i:])
                        break
                    else:
                        last_name += " " + word
                data["first_name"] = first_name
                data["last_name"] = last_name

            final_table = update_rank_sn_by_category(final_table)
            final_table = update_rank_cj_by_category(final_table)

            return True, final_table
        return False, []

    def get_results(self, event_url) -> Union[list[dict], bool]:
        """Fetches competition data using the result_url

        Example:
            client.get_results("?event_id=96")
        >>> [{'lifter': "Dave", "snatch_1": 123, 'etc':'...'}]
        """
        page_data = self._load_events_page(event_url)
        success, data = self._scrape_result_info(page_data)
        if success:
            return data
        elif not success:
            page_data = self._load_events_page(event_url, old_bw_cat=True)
            success, data = self._scrape_result_info(page_data)
            if success:
                start_time = time.time()
                time.sleep(5)
                return data
        return False
