import requests
import json


def getdata():
	users = 0
	for x in range(1,13):
		#breakpoint()
		url = "https://reqres.in/api/users?page=%d" %x
	
		response = requests.get(url = url)

		pythondata = response.json()
		data = pythondata.get('data')
		no_users = len(data)
		users = users + no_users


	
	print(users)   

getdata()





