##game/status
import requests
import json

### Key ###
api = 'b5d5bd555a1501b7324a020b229f7acdbf52afdea9bc2d5f96a74cf6d2e94780'
### playername ####
name = 'pia'
### uid ###
id = '111113'

stat = requests.get(f'http://20.196.214.79:5050/game/status?key={api}&playername={name}')
print("statusRequest:", stat.content)
print("status :", stat.status_code)

view = requests.get(f'http://20.196.214.79:5050/game/view?key={api}&uid={id}')
print("viewRequest:", view.content)
print("status :", view.status_code)