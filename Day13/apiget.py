import requests
import json
url = "http://api.open-notify.org/astros.json"
response = requests.get(url)
post_data = {
    "":"",
    "":""
}
response1 = requests.post(url,json=post_data)
