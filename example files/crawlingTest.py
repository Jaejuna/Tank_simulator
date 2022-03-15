import csv 
import json 
import requests

view_result_list = [{'info.isExistObject' : 'info.isExistObject', 'info.ObjectName' : 'info.ObjectName', 'info.ObjectType' : 'info.ObjectType', 'info.location' : 'info.location'}]

for i in range(1, 100)
  req = requests.get('http://20.196.214.79:5050/game/view')

  viewData = req.json()

  for j in viewData[objects]:
    room_list_result.append(
      {
        'info.isExistObject' : object['exist'],
        'info.ObjectName' : object['name'],
        'info.ObjectType' : object['type'],
        'info.location' : object['location']
      }
    )
with open('./view_result.csv', mode = 'w') as room_lists:
  result = csv.writer(lists)

  for k in view_result:
    result.writerow([object['exist'],object['name'],object['type'],object['location']])