class Athlete(object):
    def __init__(self, keywords=[], *args):
        self.keywords = keywords

    def _scrape_athlete_info(self):  # (self, li or soup_data)
        data = {
            "name": None,  # string
            "event": None,  # string
            "rank": None,  # int
            "category": None,  # string
            "bodyweight": None,  # float or decimal
            "snatch": None,
            "jerk": None,
            "total": None,
        }

    def get_athlete(self):
        return
