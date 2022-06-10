# -*- coding: utf-8 -*-

import requests
import time

from bs4 import BeautifulSoup
from urllib.parse import urlencode
from threading import Thread
from queue import Queue


BASE_URL = "https://iwf.sport"
HEADERS = {"Content-Type": "text/html; charset=UTF-8"}

# <---------------------------------Result------------------------------------>

# Result (Single event page)
# Example: https://iwf.sport/results/results-by-events/?event_id=529
RESULT_URL = "event_id="

# <---------------------------------Events------------------------------------>

# Event
# Example: https://iwf.sport/results/results-by-events/
EVENTS_URL = "/results/results-by-events"
OLD_BW_EVENTS_URL = "/results/results-by-events/results-by-events-old-bw"

# Event Year
# Example: https://iwf.sport/results/results-by-events/?event_year=2022
YEAR_URL = "?event_year="

# Event Filter
# Example: https://iwf.sport/results/results-by-events/?event_type=all&event_age=all&event_nation=all
EVENT_TYPE_URL = "event_type="
EVENT_AGE_URL = "event_age="
EVENT_NATION_URL = "event_nation="


# <---------------------------------Athletes---------------------------------->

# Athlete
ATHLETE_URL = "/weightlifting_/athletes-bios/"

# Athlete Search
# Example: https://iwf.sport/weightlifting_/athletes-bios/?athlete_name=test&athlete_gender=all&athlete_nation=all
ATHLETE_NAME = "athlete_name="

# Athlete Filter
ATHLETE_GENDER = "athlete_gender="
ATHLETE_NATION = "athlete_nation="


# <---------------------------------Athlete-Bio------------------------------->

# Athlete Bio (Single athlete page)
# Example: https://iwf.sport/weightlifting_/athletes-bios/?athlete=ilyin-ilya-1988-05-24&id=7895
# Must have both
ATHLETE_BIO_URL = "athlete="
ATHLETE_ID_URL = "id="


TIME_TO_WAIT = 3  # TODO: consider using Selenium WebDriver Wait API


def is_event(url):
    """
    Validates events page
    Example: https://iwf.sport/results/results-by-events/?event_type=all&event_age=all&event_nation=all
    """
    return True if EVENTS_URL or OLD_BW_EVENTS_URL in url else False


def is_result(url):
    """
    Validates event url.
    Example: https://iwf.sport/results/results-by-events/?event_id=529
    """
    return True if RESULT_URL in url else False


def is_athlete_bio(url):
    """
    Validate athlete url.
    Example: https://iwf.sport/weightlifting_/athletes-bios/?athlete=ilyin-ilya-1988-05-24&id=7895
    """
    return True if ATHLETE_BIO_URL in url else False


# def _load_new_bodyweight_events_page():
#     """
#     Loads the page for new bodyweight category
#     """
#     r = requests.get(BASE_URL + EVENTS_URL, headers=HEADERS)
#     html = r.text
#     return BeautifulSoup(html, "lxml")


# def _load_old_bodyweight_events_page():
#     """
#     Loads the page for new bodyweight category
#     """
#     r = requests.get(BASE_URL + OLD_BW_EVENTS_URL, headers=HEADERS)
#     html = r.text
#     return BeautifulSoup(html, "lxml")


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
