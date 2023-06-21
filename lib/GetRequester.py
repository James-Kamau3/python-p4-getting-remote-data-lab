import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        data_list = []
        data = json.loads(self.get_response_body())
        for i in data:
            data_list.append(i)
        return data_list

req = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
req_list = req.load_json()
print(req_list)


