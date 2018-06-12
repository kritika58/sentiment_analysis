import json

f=open("data.txt")
data=f.read()
print(type(eval(data)))
#d = json.loads(data)
#print(type(d))