# main algo
import requests
import json

## key
key = 'b5d5bd555a1501b7324a020b229f7acdbf52afdea9bc2d5f96a74cf6d2e94780'
## playerName
name = 'pia'

##status requests for to get agent info
def status():
  status = requests.get('http://20.196.214.79:5050/game/game/status?key={key}&playername={name}')
  status_object = json.loads(status.content) 
  agents = status_object["responses"]["data"]["message"]["agent_info"]["agent"] 

## uid
status()
id = agents["uid"]

##view requests for identification
# 0 = none, 1 = agent, 2 = explosive, 3 = obstacle, 4 = projectile
def view():
  view = requests.get('http://20.196.214.79:5050/game/view?key={key}&uid={id}') 
  view_object = json.loads(view.content) 
  agent_view = view_object["responses"]["data"]["message"]["info"]"] 

## move direction 
# 0 = forward, 1 = right, 2 = backward, 3 = left
view()
type = agent_view[type]

#random direction except forward
random_directoin = random.randrange(1,3)
#direction function
def direction():
  if type == 0:
    direction = 0
  elif type == 1:
    direction = random_directoin
  elif type == 2:
    direction = 2
  elif type == 3:
    direction = random_directoin
  elif name[0:2] == "SM":
    attack = requests.get('http://20.196.214.79:5050/agent/attack?key={key}&uid={id}')
  elif type == 4:
    direction = random_directoin
    
## move
def move():
  move = requests.get('http://20.196.214.79:5050/agent/move?key={key}&uid={id}&direction={direction}')
  view()

##### have to make an ai model