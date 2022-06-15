# iwf-api

A pip library to scrape filtered events and results from the IWF (International Weightlifting Federation) website.

### Methods:

- `get_years()`
- `get_events(search_url, year, new_or_old, nation, event_type, age_group)`
- `get_result(search_url)`

### Usage:

To install, type:

```
import iwf
```

To search events, type:

```
search_keywords = []
client = iwf.Iwf(search_keywords)

for event in client.get_events():
  print(event)
  print(event['name'])
```

or

```
print(Event().get_events(year='2018', new_or_old="new", age_group='Youth'))
```

to get the following results:

```
[{
	'name': '5th International Qatar Cup',
	'result_url': '?event_id=444',
	'location': 'QAT',
	'date': 'Dec 19, 2018'
}, {
	'name': '5th International Solidarity Championships',
	'result_url': '?event_id=445',
	'location': 'EGY',
	'date': 'Dec 08, 2018'
}, {
	'name': 'II International Senior CSLP Cup',
	'result_url': '?event_id=442',
	'location': 'ECU',
	'date': 'Dec 07, 2018'
}, {
	'name': 'II International Junior CSLP Cup',
	'result_url': '?event_id=443',
	'location': 'ECU',
	'date': 'Dec 07, 2018'
}, {
	'name': '2018 IWF World Championships',
	'result_url': '?event_id=441',
	'location': 'TKM',
	'date': 'Nov 01, 2018'
}]
```

To get results for an event, use the following method with an url:
```
url = "https://iwf.sport/results/results-by-events/?event_id=486"
result = client.get_results(search_url=url)
print(result)
```
and you will get:
```
[{'birthdate': 'Apr 02, 2003',
  'bodyweight': '48.88',
  'category': '49',
  'gender': 'Men',
  'group': 'A',
  'jerk': '121',
  'jerk1': '115',
  'jerk2': '121',
  'jerk3': <strike>126</strike>,
  'name': 'PAK Myong Jin',
  'nation': 'PRK',
  'rank': '1',
  'rank_cj': '1',
  'rank_sn': '1',
  'snatch': '100',
  'snatch1': '90',
  'snatch2': '96',
  'snatch3': '100',
  'total': '221'},
  ...
```

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
pip install -i https://test.pypi.org/simple/ iwf-api-jwc20
```

### Requirements:

- beautifulsoup4==4.11.1
- lxml==4.9.0
- requests==2.27.1
