## ########################################
## 00. 리시브 파일을 실행한다.
## 01. 세션 열결 확인과 API Key 생성을 한다.
## ########################################

##Session/resource
import requests
import json

resource = requests.get('http://20.196.214.79:5050/session/resource?ip=125.132.53.178')
### ip주소는 해당 사설IP주소를 입력한다. ipconfig로 확인 불가 whois 에서 확인 ###
print("createRequest:" , resource.content)
print("resource :" , resource.status_code)
json_object= json.loads(resource.content)


##Session/create
params = {"ip": "125.132.53.178", "IsWindowMode": "true", "Res_X": "680", "Res_Y": "680"}
create = requests.post('http://20.196.214.79:5050/session/create', data=params)
print("createRequest:", create.content)