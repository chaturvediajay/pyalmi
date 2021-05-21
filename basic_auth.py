import json
import requests

data1 = {'username': 'admin', 'password': 'admin'}
headers = {'Content-type': 'application/json'}
response = requests.post('https://panicdirection.herokuapp.com/authenticate', json.dumps(data1), headers=headers)
sampl=''
if response.status_code == 200:
    print('response Code ' + str(response.status_code))
    sampl = json.loads(response.text)
    print(sampl["token"])
    headers = {'Authorization': 'Bearer ' + sampl["token"], "Content-Type": "application/text"}
    payload = {}
    response = requests.get('https://panicdirection.herokuapp.com', headers=headers, data=payload)
    if response.status_code == 200:
        print('successful ' + str(response.text))
    else:
        print("unsuccessfully")
else:
    print("unsuccessfully")
