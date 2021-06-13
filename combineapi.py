
import requests
import json




URL = "https://my-json-server.typicode.com/typicode/demo/posts"
url = "https://my-json-server.typicode.com/typicode/demo/comments"


def get_data():
   
	response1 = requests.get(url= URL) 
	response2 = requests.get(url =  url) 
	

	 
	data1 = response1.json()
	data2 = response2.json()
	for i in range(len(data1)):
		
		for j in range(len(data2)):
			comment= {}
			if(data1[i].get('id') == data2[j].get('postId')):
				x = 1
				while x <= j:
					for j in range(len(data2)):
						comment[x] = data2[j]
						x = x + 1
				data1[i]['comment']= comment    

			
	json_data = json.dumps(data1)
	print(json_data)
	return json_data

get_data()    
