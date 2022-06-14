import iwf

search_keywords = []
client = iwf.Iwf(search_keywords)

for event in client.get_events():
  print(event)
  print(event['name'])

url = "https://iwf.sport/results/results-by-events/?event_id=486"
result = client.get_results(search_url=url)
print(result)