import json

x =  '{ "":""}'


table = input("Table: ").split(",")
campos = list(table)
print(campos)
z = json.loads(x)
for cam in campos:
  y = {f"{cam}":""}
  z.update(y)

a = json.dumps(z,indent=4)
print(a)
