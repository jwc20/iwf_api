from .core import *
import json

# TODO: add method for combining year and other filters


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
        search_url = ""
        if url and is_event(url):
            r = requests.get(url, headers=HEADERS)

        if new_or_old:
            search_url = self._craft_bodyweight_url(new_or_old)

        filters = []
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
        search_url += "/?" + filters[0]
        if len(filters) > 1:
            for i in range(1, len(filters)):
                search_url += "&" + filters[i]
        return search_url

    def _load_event_page(self, search_url):
        r = requests.get(search_url, headers=HEADERS)

        html = r.text
        return BeautifulSoup(html, "lxml")

    # def _scrape_event_type(self):
    #     return

    # def _scrape_event_age_group(self):
    #     return

    # def _scrape_event_nation(self):
    #     return

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
            "result_url": None,  # string
            "location": None,  # string
            "date": None,  # string
        }

        cards = soup_data.findAll("a", {"class": "card"})

        for card in cards:
            data["name"] = card.find("span", {"class": "text"}).string
            data["result_url"] = card["href"]
            # print(card['href'])
            data["location"] = card.find("strong").string
            data["date"] = card.find("p", {"class": "normal__text"}).string.strip()
            print(
                card.find("p", {"class": "normal__text"})
                .string.strip()
            )

        # data["name"] = soup_data.find("span").find("text")
        # print()

        return data

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
