import requests

#input_ıd=input("Enter Id: ")
#get_url=f"https://jsonplaceholder.typicode.com/todos/{input_ıd}"
#get_response=requests.get(get_url)
#print(get_response.json())

tod_do_item={"userId":2, "title":"my todo","completed":False}
post_url="https://jsonplaceholder.typicode.com/todos"
post_response=requests.post(post_url,tod_do_item)
print(post_response.json())
