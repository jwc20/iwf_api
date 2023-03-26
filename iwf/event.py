import requests

from bs4 import BeautifulSoup
import re

from .core import eBase, eHeaders, eEvents, is_event


class Event(object):
    def __init__(self, keywords=[], *args):
        self.keywords = keywords

    def _craft_url(
        self,
        new_or_old=None,
        year=None,
        nation=None,
        event_type=None,
        age_group=None,
    ):

        filters = []
        if new_or_old == "old":
            search_url = eBase.URL + eEvents.OLD_BW_URL
        else:
            search_url = eBase.URL + eEvents.URL

        # TODO: Combine years results with other filters
        if year:
            search_url += eEvents.YEAR_URL + year
        else:
            if event_type:
                if " " in event_type:
                    event_type_new = event_type.replace(" ", "+")
                    filters.append(eEvents.TYPE_URL + event_type_new)
            if age_group:
                filters.append(eEvents.AGE_URL + age_group)
            if nation:
                filters.append(eEvents.NATION_URL + nation)

        if len(filters) >= 1:
            search_url += "/?" + filters[0]
            for i in range(1, len(filters)):
                search_url += "&" + filters[i]
        print(search_url)
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
            r = requests.get(search_url, headers=eHeaders.PAYLOAD)
        else:
            new_url = self._craft_url(
                new_or_old,
                year,
                nation,
                event_type,
                age_group,
            )
            r = requests.get(new_url, headers=eHeaders.PAYLOAD)

        html = r.text
        return (new_url, BeautifulSoup(html, "lxml"))

    def _scrape_event_info(self, soup_data):
        result = []
        cards = soup_data[1].findAll("a", {"class": "card"})
        result_base_url = re.sub(r'\?.*', '', soup_data[0])
        print(result_base_url)
        for card in cards:
            data = {
                "name": None,  # string
                "result_url": None,  # string
                "location": None,  # string
                "date": None,  # string
            }
            data["name"] = card.find("span", {"class": "text"}).string
            # data["result_url"] = card["href"]
            data["result_url"] = result_base_url + card["href"]
            data["location"] = card.find("strong").string
            data["date"] = card.find("p", {"class": "normal__text"}).string.strip()
            result.append(data)
        return result

    def get_events(
        self,
        search_url=None,
        year=None,
        new_or_old=None,
        nation=None,
        event_type=None,
        age_group=None,
    ):
        result_data = self._scrape_event_info(
            self._load_event_page(
                search_url, new_or_old, year, nation, event_type, age_group
            )
        )
        if result_data:
            return result_data

    # Temporarily fetch years
    # TODO: Figure out using the functions in core.py

    def _scrape_select_years(self, page):
        """
        Scrapes data for new or old bodyweight page
        """
        select_option = page.findAll("select", {"name": "event_year"})[0]
        options = select_option.findAll("option")
        years = []
        for item in options:
            years.append(item.get_text())

        return years

    def _load_old_bodyweight_events_page(self):
        """
        Loads the page for new bodyweight category
        """
        r = requests.get(eBase.URL + eEvents.OLD_BW_URL, headers=eHeaders.PAYLOAD)
        html = r.text
        return BeautifulSoup(html, "lxml")

    def get_years(self):
        """
        Gets all years available.
        New bodyweight years not needed since old bodyweight <select> includes them
        """
        old_events_years = self._scrape_select_years(
            self._load_old_bodyweight_events_page()
        )
        return old_events_years
