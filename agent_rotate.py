# agent_rotate
import requests

##status requests for to get agent info
status = requests.get('http://20.196.214.79:5050/game/game/view?key={key}&playername={name}')
json_object = json.loads(status.content) 
agents = json_object["data"]["message"]["agent_info"]["agent"] 

## key
key = 'b5d5bd555a1501b7324a020b229f7acdbf52afdea9bc2d5f96a74cf6d2e94780'
## uid
id = agent_info[uid]
## angle
angle = 45

####### have to rotate on right situation
####### rotating till view object type SM will do
rotate = requests.get('http://20.196.214.79:5050/agent/rotate?key={key}&uid={id}&angle={angle}')