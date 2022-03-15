# agent_move
import requests
import json

## key
key = 'b5d5bd555a1501b7324a020b229f7acdbf52afdea9bc2d5f96a74cf6d2e94780'
## playerName
name = 'pia'
## uid
id = '111113'

status = requests.get('http://20.196.214.79:5050/game/status?key={key}&playername={}') 
json_object = json.loads(status.content) agents = json_object["data"]["message"]["agent_info"]["agent"] 

# have to make move algorithm
attack = requests.get('http://20.196.214.79:5050/agent/move?key={key}&uid={id}')