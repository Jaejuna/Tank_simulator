import requests
import json 

#game/endturn
def endturn():
    key = 'b5d5bd555a1501b7324a020b229f7acdbf52afdea9bc2d5f96a74cf6d2e94780' 
    player = "P1"      
    params = {
        "key": key,
        "player": player
    }
    endTurn = requests.post('http://20.196.214.79:5050/game/endturn', data = params)
    print('Ended turn!')

#game/giveup
def giveup():
    key = 'b5d5bd555a1501b7324a020b229f7acdbf52afdea9bc2d5f96a74cf6d2e94780' 
    player = "P1"      
    params = {
        "key": key,
        "player": player
    }
    giveup = requests.post('http://20.196.214.79:5050/game/giveup', data = params)
    print('gave up the game!')

#game/status
def status(): 
    key = 'b5d5bd555a1501b7324a020b229f7acdbf52afdea9bc2d5f96a74cf6d2e94780' 
    player = "P1"      
    params = {
        "key": key,
        "player": player
    }

    status = requests.get('https://20.196.214.79:5050/game/status', data = params)
    json_object = json.loads(status.content)
    agents = json_object["data"]["message"]["agent_info"]["agent"]

#game/view
def view():
    key = 'b5d5bd555a1501b7324a020b229f7acdbf52afdea9bc2d5f96a74cf6d2e94780' 
    player = "P1"      
    params = {
        "key": key,
        "player": player
    }

    view = requests.get('http://20.196.214.79:5050/game/view', data = params)
    json_object = json.loads(view.content)
    print("data.message:", json_object["Info"])