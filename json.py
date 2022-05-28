import json


import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])





# a Python object (dict):
w = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
z = json.dumps(w)

# the result is a JSON string:
print(z)






#DESPLEGANDO UN DICCIONARIO EN FORMATO JSON
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# convert into JSON:
y = json.dumps(x, indent=4)

# the result is a JSON string:
print(y)





# CONVIERTE CADENAS DE TEXTO A JSON
x = '''{
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}'''

# convert into JSON:
y = json.load(x)
# the result is a JSON string:
print(y)




# acepta cualquier tipo de dato
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))







#SOME FUNCTIONS WITH JSON
x = []

def hello():
    datos = input("ingresa los datos: ")
    campos = str(datos).split(",")
    com = re.findall(";$",datos)
    if com:
        for cam in campos:
            y = {f"{cam}":""}
            y = str(f'"{y}"')
            x.append(y)
            j = json.dumps(x,indent=4)
            print(j)
    else:
        for cam in campos:
            y = {f"{cam}":""}
            x.append(y)
            hello()






def testt():
      # try:
    datos = input("ingresa los datos: ")
    com = re.findall(";$",datos)

    campos = datos.split(",")
    campos = tuple(campos)

    a = []
    if com:
        for cam in campos:
            cam = ' '
            a.append(cam)

        a = tuple(a)
        w = dict(zip(campos,a))
        j = json.dumps(w,indent=4)
        print(j)
    else:
        testt()
  # except:
  #   print(NameError)

testt()





