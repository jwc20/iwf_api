import core


class Event(object):
    def __init__(self, keywords=[], *args):
        self.keywords = keywords

    def _scrape_event_info(self): # (self, li or soup_data)
        data = {
            "name": None,  # string
            "url": None,  # string
            "location": None,  # string
            "date": None,  # string
        }

    def get_events(self, year=None, new_or_old=None, bodyweight=None, quantity=None, infinity=False, sort_by=None, nation=None, event_type=None, age_group=None):
        return 0
