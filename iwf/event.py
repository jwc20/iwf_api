from .core import *
import json


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
        search_url = ""
        filters = []
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

    def _scrape_event_info(self, soup_data):
        result = []
        cards = soup_data.findAll("a", {"class": "card"})
        for card in cards:
            data = {
                "name": None,  # string
                "result_url": None,  # string
                "location": None,  # string
                "date": None,  # string
            }
            data["name"] = card.find("span", {"class": "text"}).string
            data["result_url"] = card["href"]
            data["location"] = card.find("strong").string
            data["date"] = card.find("p", {"class": "normal__text"}).string.strip()
            result.append(data)
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
        result_data = self._scrape_event_info(
            self._load_event_page(
                search_url, new_or_old, year, nation, event_type, age_group
            )
        )
        if result_data:
            return result_data

    def _scrape_event_type(self):
        return

    def _scrape_event_age_group(self):
        return

    def _scrape_event_nation(self):
        return
