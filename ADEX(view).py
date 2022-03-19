##game/view/status/attack
import requests
import json
import random

view = requests.get(
    'http://20.196.214.79:5050/game/view?key=b5d5bd555a1501b7324a020b229f7acdbf52afdea9bc2d5f96a74cf6d2e94780&uid=109319')
json_object = json.loads(view.content)
print(json_object["responses"]["data"]["message"]["info"])