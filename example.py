from pprintpp import pprint
import iwf

client = iwf.Iwf()

# for event in client.get_events():
#   print(event)
# print(event['name'])

# url = "https://iwf.sport/results/results-by-events/?event_id=535"
url = "https://iwf.sport/results/results-by-events/results-by-events-old-bw/?event_id=4"
result = client.get_results(event_url=url)
pprint(result)


# with open("result.txt", "w") as f: 
#     f.write(str(result))
