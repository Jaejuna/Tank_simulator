##game/agent
import requests
import json
import random

status = requests.get('http://20.196.214.79:5050/game/status?key=b5d5bd555a1501b7324a020b229f7acdbf52afdea9bc2d5f96a74cf6d2e94780&playername=pia')
json_object = json.loads(status.content)
agents = json_object["responses"]["data"]["message"]["agent_info"]["agent"]
for idx in range(4):
    agentInfo = agents[idx]
    #전차의객체들을하나씩랜덤값으로기동
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
      "key": "b5d5bd555a1501b7324a020b229f7acdbf52afdea9bc2d5f96a74cf6d2e94780",
      "uid": agentInfo["uid"],
      "direction": direction
    }
    move = requests.post('http://20.196.214.79:5050/agent/move', data = moveParams)

    attackParms = {
      "key": "b5d5bd555a1501b7324a020b229f7acdbf52afdea9bc2d5f96a74cf6d2e94780",
      "uid": agentInfo["uid"]
    }
    attack = requests.get('http://20.196.214.79:5050/agent/attack',data=attackParms)
    print(agentInfo["name"], " -> ", dirTxt)