# from iwf.core import *
# from bs4 import BeautifulSoup
# from urllib.parse import urlencode
# from threading import Thread
# from queue import Queue

# <---------------------------------Validations------------------------------->


# def isResult(url):
#     """
#     Validates event url.
#     Example: https://iwf.sport/results/results-by-events/?event_id=529
#     """
#     return True if RESULT_URL in url else False
# 
# 
# def isAthleteBio(url):
#     """
#     Validate athlete url.
#     Example: https://iwf.sport/weightlifting_/athletes-bios/?athlete=ilyin-ilya-1988-05-24&id=7895
#     """
#     return True if ATHLETE_BIO_URL in url else False
# 
# 
# def _loadNewBodyweightEventsPage():
#     """
#     Loads the page for new bodyweight category
#     """
#     r = requests.get(BASE_URL + EVENTS_URL, headers=HEADERS)
#     html = r.text
#     return BeautifulSoup(html, "lxml")
# 
# 
# def _loadOldBodyweightEventsPage():
#     """
#     Loads the page for new bodyweight category
#     """
#     r = requests.get(BASE_URL + OLD_BW_EVENTS_URL, headers=HEADERS)
#     html = r.text
#     return BeautifulSoup(html, "lxml")
# 
# 
# def _scrapeSelectYears(page):
#     """
#     Scrapes data for new or old bodyweight page
#     """
#     select_option = page.findAll("select", {"name": "event_year"})[0]
#     options = select_option.findAll("option")
#     years = []
#     for item in options:
#         years.append(item.get_text())
# 
#     return years
# 
# 
# def getYears():
#     """
#     Gets all years available.
#     New bodyweight years not needed since old bodyweight includes them
#     """
# 
#     # old_bw = []
#     # for year in _scrapeSelectYears(_loadOldBodyweightEventsPage):
#     #     if year <= 2018:
#     #         old_bw.append(year)
# 
#     # new_events_years = [_scrapeSelectYears(_loadNewBodyweightEventsPage())]
#     old_events_years = [_scrapeSelectYears(_loadOldBodyweightEventsPage())]
# 
# 
#     for i in range(len(old_events_years)):
#         if old_events_years[i]:
#             print(old_events_years[i])
# 
#     return 0
# 
# 
# """
# print(_scrapeSelectYears(_loadNewBodyweightEventsPage()))
# print(_scrapeSelectYears(_loadOldBodyweightEventsPage()))
# """
# 
# print(getYears())
