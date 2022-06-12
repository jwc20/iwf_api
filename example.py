import iwf

search_keywords = []


client = iwf.Iwf(search_keywords)


for event in client.get_events():
  print(event)
  print(event['name'])
