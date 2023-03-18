import iwf

client = iwf.Iwf()

# for event in client.get_events():
#   print(event)
#   print(event['name'])

url = "https://iwf.sport/results/results-by-events/?event_id=535"
result = client.get_results(event_url=url)
print(result)
