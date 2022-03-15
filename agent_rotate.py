# agent_rotate
import requests

## key
key = 'b5d5bd555a1501b7324a020b229f7acdbf52afdea9bc2d5f96a74cf6d2e94780'
## uid
id = '111113'
## angle
angle = 45

####### have to rotate on right situation
attack = requests.get('http://20.196.214.79:5050/agent/rotate?key={key}&uid={id}&angle={angle}')