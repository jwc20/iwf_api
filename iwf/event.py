from .core import *
import json


class Event(object):
    def __init__(self, keywords=[], *args):
        self.keywords = keywords

    def _craft_bodyweight_url(new_or_old=None):
        if new_or_old == "old":
            return BASE_URL + OLD_BW_EVENTS_URL
        else:
            return BASE_URL + EVENTS_URL

    def _craft_url(
        self,
        url=None,
        new_or_old=None,
        year=None,
        nation=None,
        event_type=None,
        age_group=None,
    ):

        if url and is_event(url):
            r = requests.get(url, headers=HEADERS)

        else:
            search_url = self._craft_bodyweight_url(new_or_old)
            filters = []
            if year:
                search_url += YEAR_URL
            else:
                if event_type:
                    filters.append(EVENT_TYPE_URL + event_type)
                elif age_group:
                    filters.append(EVENT_AGE_URL + age_group)
                elif nation:
                    filters.append(EVENT_NATION_URL + nation)
            # search_url += "&".join(filters)
            for i in range(len(filters)):
                if i == 0:
                    search_url += "?" + filters[0]
                search_url += "&" + filters[i]
        return

    def _load_event_page(self, search_url):
        r = requests.get(search_url, headers=HEADERS)

        html = r.text
        return BeautifulSoup(html, "lxml")

    _load_event_page(year=2022)

    def _scrape_event_type(self):
        return

    def _scrape_event_age_group(self):
        return

    def _scrape_event_nation(self):
        return

    def _scrape_event_div_card(self):
        """
        <div class="cards">
            <a href="?event_id=529" class="card">
            ...
        </div>
        """
        return

    def _scrape_event_info(self):  # (self, li or soup_data)
        data = {
            "name": None,  # string
            "url": None,  # string
            "location": None,  # string
            "date": None,  # string
        }
        return

    def get_events(
        self,
        year=None,
        new_or_old=None,
        bodyweight=None,
        quantity=None,
        infinity=False,
        sort_by=None,
        nation=None,
        event_type=None,
        age_group=None,
    ):
        return 0
