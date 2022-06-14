from .core import *
import json
import re

# from lxml import html
from lxml import etree


class Result(object):
    def __init__(self, keywords=[], *args):
        self.keywords = keywords

    def _load_result_page(self, search_url):
        r = requests.get(search_url, headers=HEADERS)
        html = r.text
        return BeautifulSoup(html, "lxml")

    def _scrape_result_info(self, soup_data):
        result = []

        result_container = soup_data.find_all("div", {"class": "result__container"})
        for div_id in result_container:

            # id="men_total"
            # men_snatchjerk
            # women_total
            # women_snatchjerk

            # print(len(result_container))
            # print(div_id if div_id.get("id") == "men_snatchjerk" else "ACK")

            if (
                div_id.get("id") == "men_snatchjerk"
                or div_id.get("id") == "women_snatchjerk"
            ):

                category = div_id.find_all("div", {"class": "col-12"})

                # data["name"] = (
                #     div_id.find("div", {"class": "col-7 not__cell__767"})
                #     .find("p")
                #     .text.strip()
                # )

                count = 0
                for item in category:
                    h3_cat = item.find("h3")
                    if h3_cat:
                        # print(item)
                        cards_container = div_id.find_all("div", {"class": "cards"})

                        # getting the names, nation, birthdate, bodyweight, group
                        for cards in cards_container[::3]:

                            # print(cards.find_all("div", {"class": "col-7 not__cell__767"}))
                            # card_container = cards.find_all("div", {"class": "col-7 not__cell__767"})
                            card_container = cards.find_all("div", {"class": "card"})




                            
                            for card in card_container[1:]:

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

                                # print(card)
                                # p_tags = card.find_all('p')[1]
                                # p_tags_name = 
                                # print(p_tags_name)
                                # print(card.find_all("p"))
                                data["name"] = card.find_all("p")[1].text.strip()
                                data["nation"] = card.find_all("p")[2].text.strip()
                                data["birthdate"] = card.find_all("p")[3].text.strip()
                                data["bodyweight"] = card.find_all("p")[4].text.strip()
                                data["group"] = card.find_all("p")[5].text.strip()
                                data["snatch1"] = card.find_all("p")[6].text.strip().split()[1]
                                data["snatch2"] = card.find_all("p")[7].text.strip().split()[1]
                                data["snatch3"] = card.find_all("p")[8].text.strip().split()[1]    
                                data["snatch"] = card.find_all("p")[9].text.strip().split()[1]
                            # print(card_container[0].parent.previous_sibling.previous_sibling.previous_sibling.previous_sibling.text.strip())
                            # print(cards.previous_sibling.previous_sibling.previous_sibling.previous_sibling.text.strip())
                                data["category"] = card.parent.previous_sibling.previous_sibling.previous_sibling.previous_sibling.text.strip()


                                # sn = card.find_all("p")[9].text.strip()
                                # data["snatch"] = re.search(r"\d+", sn)
                                # print(p_tags_name.text.strip())

                                # print(type(p_tags))

                                result.append(data)
                            # print(
                            #     "#####################################end of cards######################################"
                            # )

                            # print(p_tags)

                            # for p_tag in p_tags:
                            #     print("########################",p_tag)

                            # name = p_tags[1]
                            # print(name)
                            # data["name"] =

                            # print(p_tags)
                            # for p_tag in p_tags:
                            #     # print(p_tag.text.strip())
                            #     print(count, p_tag)

                            # count += 1

                            # data["name"] = name
                            # print(card.find_all('p')[1].text.strip())
                            # data["nation"] = card.find()
                        # names = div_id.find_all("div", {"class": "col-7 not__cell__767"})
                        # for name in names:
                        #     print(name.find('p').text.strip())
                        # print(count, div_id.find("div", {"class": "col-7 not__cell__767"}).find("p").text.strip())
                        # count += 1
                        # print(count)
                # print(div_id.find("div", {"class": "col-7 not__cell__767"}).find("p").text.strip())
                # print(count)
                # result.append(data)

                # for div_cl in div_id.findAll("div"):

                #     name_container = div_cl.find("div", {"class": "col-7 not__cell__767"})
                #     if name_container:
                #         name = name_container.find("p").string.strip()
                #         data["name"] = name
                #         data["nation"] = (
                #             div_cl.find("div", {"class": "col-3 not__cell__767"})
                #             .find("p")
                #             .text.strip()
                #         )

                # if category:
                #     data["category"] = category.text.strip()
                # for res_cont in div_cl.parent.find_all("h2"):
                #     data["category"] = res_cont.text
                #     print(res_cont)
                # print(res_cont)
                #     # print(sibling)
                #     print(res_cont.find('div', {'class': 'col-12'}))
                #     # category = res_cont.find('div', {'class': 'col-12'})
                #     # if category:
                #     #     print(category)

                # print(div_cl.parent.find_all("h2"))

                # result.append(data)

                # if div_cl.previous_sibling.find('p') == 'Snatch':
                #     print('ack')
                # print(name)
                # print(name.find('p').text.strip())
                # if name in data

        return result

        # cards = soup_data.select("div.cards")
        # results = []

        # cards_list = soup_data.find_all('div', {'class': 'cards'})
        # # print(row_list)
        # for card in cards_list:
        #     for car in card.find_all('div', {'class': 'card'}):
        #         data = {
        #             "name": None,  # string
        #             "birthdate": None,  # string
        #             "nation": None,  # string
        #             "athlete_url": None,  # string
        #             "category": None,  # string
        #             "bodyweight": None,  # string
        #             "group": None,  # string
        #             "snatch1": None,  # string
        #             "snatch2": None,  # string
        #             "snatch3": None,  # string
        #             "snatch": None,  # string
        #             "jerk1": None,  # string
        #             "jerk2": None,  # string
        #             "jerk3": None,  # string
        #             "jerk": None,  # string
        #             "total": None,  # string
        #             "rank_sn": None,  # string
        #             "rank_cj": None,  # string
        #             "rank": None,  # string
        #         }
        #         # print(car)
        #         name = car.find("div", {"class": "col-7 not__cell__767"})
        #         # print(name)
        #         if name and name != None:
        #             # print(name)
        #             data["name"] = name.find('p').text.strip()
        #         # name = car.find("div", {"class": "col-7 not__cell__767"}).find('p').text.strip()
        #         # if name:
        #         #     data["name"] = name
        #         # print(name)
        #         # print(car)

        #     results.append(data)

        # return results

    def get_results(self):
        return
