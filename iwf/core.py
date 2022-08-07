import requests

from enum import Enum
from bs4 import BeautifulSoup


class eBase(str, Enum):
    """
    Stores the base URL
    """
    URL = "https://iwf.sport"


class eHeaders(dict, Enum):
    """
    Headers required for requests payloads
    """
    PAYLOAD = {"Content-Type": "text/html; charset=UTF-8"}


class eResult(str, Enum):
    """
    Result (Single event page)
    Example: https://iwf.sport/results/results-by-events/?event_id=529
    """
    URL = "event_id="


class eEvents(str, Enum):
    """
    Event str enum for URL strings
    """
    URL = "/results/results-by-events"
    OLD_BW_URL = "/results/results-by-events/results-by-events-old-bw"
    YEAR_URL = "?event_year="
    TYPE_URL = "event_type="
    AGE_URL = "event_age="
    NATION_URL = "event_nation="


class eAthlete(str, Enum):
    """
    Athlete str enum for URL strings
    """
    URL = "/weightlifting_/athletes-bios/"
    NAME = "athlete_name="
    GENDER = "athlete_gender="
    NATION = "athlete_nation="


class eAthleteBio(str, Enum):
    """
    Athlete Bio (Single athlete page)
    Example: https://iwf.sport/weightlifting_/athletes-bios/?athlete=ilyin-ilya-1988-05-24&id=7895
    Must have both"""
    URL = "athlete="
    ID = "id="


def is_event(url):
    """
    Validates events page
    Example: https://iwf.sport/results/results-by-events/?event_type=all&event_age=all&event_nation=all
    """
    return True if eEvents.URL or eEvents.OLD_BW_URL in url else False


def is_result(url):
    """
    Validates event url.
    Example: https://iwf.sport/results/results-by-events/?event_id=529
    """
    return True if eResult.URL in url else False


def is_athlete_bio(url):
    """
    Validate athlete url.
    Example: https://iwf.sport/weightlifting_/athletes-bios/?athlete=ilyin-ilya-1988-05-24&id=7895
    """
    return True if eAthleteBio.URL in url else False


def _load_new_bodyweight_events_page():
    """
    Loads the page for new bodyweight category
    """
    r = requests.get(eBase.URL + eEvents.URL, headers=eHeaders.PAYLOAD)
    html = r.text
    return BeautifulSoup(html, "lxml")


def _load_old_bodyweight_events_page():
    """
    Loads the page for new bodyweight category
    """
    r = requests.get(eBase.URL + eEvents.OLD_BW_URL, headers=eHeaders.PAYLOAD)
    html = r.text
    return BeautifulSoup(html, "lxml")


def _scrape_select_years(page):
    """
    Scrapes data for new or old bodyweight page
    """
    select_option = page.findAll("select", {"name": "event_year"})[0]
    options = select_option.findAll("option")
    years = []
    for item in options:
        years.append(item.get_text())

    return years


def get_years():
    """
    Gets all years available.
    New bodyweight years not needed since old bodyweight <select> includes them
    """
    old_events_years = _scrape_select_years(_load_old_bodyweight_events_page())
    return old_events_years


def _scrape_event_type():
    types = []
    page = _load_new_bodyweight_events_page().find("select", {"name": "event_type"})
    for option in page.find_all("option"):
        if option.has_attr("value") and option["value"] != "all":
            types.append(option.text)
    return types


def _scrape_event_age_group():
    age_groups = []
    page = _load_new_bodyweight_events_page().find("select", {"name": "event_age"})
    for option in page.find_all("option"):
        if option.has_attr("value") and option["value"] != "all":
            age_groups.append(option.text)
    return age_groups


def _scrape_event_nation():
    nations = []
    page = _load_new_bodyweight_events_page().find("select", {"name": "event_nation"})
    for option in page.find_all("option"):
        if option.has_attr("value") and option["value"] != "all":
            nations.append(option.text)
    return nations
