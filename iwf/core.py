# -*- coding: utf-8 -*-

import requests
import time
from iwf.helper import *

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
YEAR_URL = "event_year="

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


def isResult(url):
    """
    Validates event url.
    Example: https://iwf.sport/results/results-by-events/?event_id=529
    """
    return True if RESULT_URL in url else False


def isAthleteBio(url):
    """
    Validate athlete url.
    Example: https://iwf.sport/weightlifting_/athletes-bios/?athlete=ilyin-ilya-1988-05-24&id=7895
    """
    return True if ATHLETE_BIO_URL in url else False


def _loadNewBodyweightEventsPage():
    """
    Loads the page for new bodyweight category
    """
    r = requests.get(BASE_URL + EVENTS_URL, headers=HEADERS)
    html = r.text
    return BeautifulSoup(html, "lxml")


def _loadOldBodyweightEventsPage():
    """
    Loads the page for new bodyweight category
    """
    r = requests.get(BASE_URL + OLD_BW_EVENTS_URL, headers=HEADERS)
    html = r.text
    return BeautifulSoup(html, "lxml")


def _scrapeSelectYears(page):
    """
    Scrapes data for new or old bodyweight page
    """
    select_option = page.findAll("select", {"name": "event_year"})[0]
    options = select_option.findAll("option")
    years = []
    for item in options:
        years.append(item.get_text())

    return years


def getYears():
    """
    Gets all years available.
    New bodyweight years not needed since old bodyweight <select> includes them
    """

    # old_bw = []
    # for year in _scrapeSelectYears(_loadOldBodyweightEventsPage):
    #     if year <= 2018:
    #         old_bw.append(year)

    # new_events_years = [_scrapeSelectYears(_loadNewBodyweightEventsPage())]
    old_events_years = [_scrapeSelectYears(_loadOldBodyweightEventsPage())]

    for i in range(len(old_events_years)):
        if old_events_years[i]:
            print(old_events_years[i])

    return 0


"""
print(_scrapeSelectYears(_loadNewBodyweightEventsPage()))
print(_scrapeSelectYears(_loadOldBodyweightEventsPage()))
"""

print(getYears())
