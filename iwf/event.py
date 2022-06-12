from .core import *
import json


class Event(object):
    def __init__(self, keywords=[], *args):
        self.keywords = keywords

    def _craft_bodyweight_url(self, new_or_old):
        if new_or_old == "old":
            return BASE_URL + OLD_BW_EVENTS_URL
        # if new_or_old == "new":
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
        search_url = ''
        if url and is_event(url):
            r = requests.get(url, headers=HEADERS)

        if new_or_old:
          search_url = self._craft_bodyweight_url(new_or_old)

        filters = []
        if year:
            search_url += YEAR_URL + year
        else:
            if event_type:
                if ' ' in event_type:
                  print('has space')
                  print(event_type)
                  event_type_new = event_type.replace(' ', '+')
                  print(event_type_new)
                  filters.append(EVENT_TYPE_URL + event_type_new)
            elif age_group:
                filters.append(EVENT_AGE_URL + age_group)
            elif nation:
                filters.append(EVENT_NATION_URL + nation)
        # search_url += "&".join(filters)
        print(len(filters))
        for i in range(len(filters)):
            if len(filters) == 1:
                search_url += "/?" + filters[0]
                return search_url
            else:
              search_url += "&" + filters[i]
              return search_url
        # return search_url

    def _load_event_page(self, search_url):
        r = requests.get(search_url, headers=HEADERS)

        html = r.text
        return BeautifulSoup(html, "lxml")

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

    def _scrape_event_info(self, soup_data):  # (self, li or soup_data)
        data = {
            "name": None,  # string
            "url": None,  # string
            "location": None,  # string
            "date": None,  # string
        }

        # data["name"] =

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
