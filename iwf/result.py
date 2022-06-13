from .core import *
import json


class Result(object):
    def __init__(self, keywords=[], *args):
        self.keywords = keywords


    def _load_result_page(self, search_url):
        r = requests.get(search_url, headers=HEADERS)
        html = r.text
        return BeautifulSoup(html, 'lxml')


    def _scrape_result_info(self, soup_data):
        result = []
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

        return



    def get_results(self):
        return
