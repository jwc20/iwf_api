# iwf-api

A pip library to scrape filtered events and results from the IWF (International Weightlifting Federation) website.

### Methods:

- `get_events(search_url, year, new_or_old, nation, event_type, age_group)`
- `get_result(search_url)`

### Scraped Data:

#### Event:

- name
- location
- date
- url

#### Result:

- name
- nation
- birthdate
- bodyweight
- category_number
- gender
- group
- snatch1
- snatch2
- snatch3
- snatch
- rank_sn
- jerk1
- jerk2
- jerk3
- jerk
- rank_cj
- total
- rank

### Installation:

To install, pip install into python virtual environment.

```
pip install git+https://github.com/jwc20/iwf-api.git
```

### Requirements:

- beautifulsoup4==4.11.1
- lxml==4.9.0
- requests==2.27.1
