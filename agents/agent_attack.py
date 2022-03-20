# agent_attack
import requests

## key
key = 'b5d5bd555a1501b7324a020b229f7acdbf52afdea9bc2d5f96a74cf6d2e94780'
## uid
id = '111113'

attack = requests.get('http://20.196.214.79:5050/agent/attack?key={key}&uid={id}')