import json
import requests
jsonurl = 'http://0.0.0.0:5000/api/'
data = [[4.2, 2.8, 1.7, 0.38]]
j_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(jsonurl, data=j_data, headers=headers)
print(r,r.text)