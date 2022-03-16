##Session/join -> game/start
import requests
import json

key = "b5d5bd555a1501b7324a020b229f7acdbf52afdea9bc2d5f96a74cf6d2e94780"
params= {"key":key, "playername":"pia"}
join = requests.post('http://20.196.214.79:5050/session/join' ,data = params)
if (join.status_code== 200):
    print("join Success!")
    startParams= {"key":key,"turn":100,"dilation":5}
    join = requests.post('http://20.196.214.79:5050/game/start' ,data = startParams)
    if (join.status_code == 200):
        print("game start")
    else:
        print("game start Error")
else:
    print("join Error")