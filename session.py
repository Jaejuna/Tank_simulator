import requests
import json 

# session/resource
resource = requests.get('https://20.196.214.79:5050/session/resource')
print("createRequest:", resource.content)
print("resource:", resource.status_code)
json_object = json.loads(resource.contect)
print("data.message:", json_object["data"]["message"])

# session/create
params = {
    "ip": "20.196.214.79",
    "IsWindowMode":"true", 
    "Res_X":"498", 
    "Res_y":"498"
    }
create = requests.post('https://20.196.214.79:5050/session/create', date = params)
print("createRequest:", create.content)

# session/join
key = ' '       #서버 통신을 위한 비밀키
params = {
    "key": key,
    "player": "P1"
}
join = requests.post('http://20.196.214.79/session/join', data = params)
if (join.status_code == 200):
    print('join success!')
    # game/start
    gameStartParams = {
        "key" : key,
        "trun" : 100,
        "dialation": 5
        }
    join = requests.post('http://20.196.214.79/game/start', data = startParams)
    if (join.status_code == 200):
        print('game start!')
    else:
        print("game start failed")
else:
    print('session join failed')