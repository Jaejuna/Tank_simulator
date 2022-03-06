import requests
import json 

# session/create
def create():
    params = {
        "ip": "20.196.214.79",
        "IsWindowMode":"true", 
        "Res_X":"498", 
        "Res_y":"498"
        }
    create = requests.post('https://20.196.214.79:5050/session/create', date = params)
    print("createRequest:", create.content)

# session/resource
def resource():
    resource = requests.get('https://20.196.214.79:5050/session/resource', verify = False)
    print("createRequest:", resource.content)
    print("resource:", resource.status_code)
    json_object = json.loads(resource.content)
    print("data.message:", json_object["data"]["message"])

# session/end
def end():
    key = 'b5d5bd555a1501b7324a020b229f7acdbf52afdea9bc2d5f96a74cf6d2e94780'       
    resource = requests.post('https://20.196.214.79:5050/session/end', key)
    print("game ended")

# session/reset
def reset():
    key = 'b5d5bd555a1501b7324a020b229f7acdbf52afdea9bc2d5f96a74cf6d2e94780'       
    resource = requests.post('https://20.196.214.79:5050/session/reset', key)
    print("program reseted")



# session/join
#서버 통신을 위한 비밀키
def join():
    key = 'b5d5bd555a1501b7324a020b229f7acdbf52afdea9bc2d5f96a74cf6d2e94780'       
    params = {
        "key": key,
        "player": "P1"
    }
    join = requests.post('http://20.196.214.79/session/join', data = params, verify = False)
    if (join.status_code == 200):
        print('join success!')
        # game/start
        gameStartParams = {
            "key" : key,
            "trun" : 100,
            "dialation": 5
            }
        join = requests.post('http://20.196.214.79/game/start', data = gameStartParams, verify = False)
        if (join.status_code == 200):
            print('game start!')
        else:
            print("game start failed")
    else:
        print('session join failed')