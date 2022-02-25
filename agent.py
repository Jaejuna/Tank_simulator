import requests
import json 

key = ' '       #서버 통신을 위한 비밀키
statusParam = {
    "key" : key,
    "playerName" : "P1"
}

status = requests.get('https://20.196.214.79:5050/game/status', data = statusParam)
json_object = json.loads(status.content)
agents = json_object["data"]["message"]["agent_info"]["agent"]
for idx in range(4):
    agentInfo = agents[idx]
    direction = random.randrange(0,3)
    if direction == 0:
        dirTxt = "Foward"
    elif direction == 1:
        dirTxt = "Left"
    elif direction == 2:
        dirTxt = "Back"
    elif direction == 3:
        dirTxt = "Right"
    moveParams = {
        "key" : key,
        "uid" : agentInfo["uid"],
        "direction" : direction
    }
    move = requests.post('https://20.196.214.79:5050/agent/move', data = moveParams)
    print(agentInfo["name"], " = ", dirTxt)