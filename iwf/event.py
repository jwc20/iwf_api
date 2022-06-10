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

    def _load_event_page(
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
            # r = requests.get(search_url)
            print(search_url, filters)
        return 0
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
