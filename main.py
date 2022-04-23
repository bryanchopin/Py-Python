

import json,re







def json():
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

file = "file.dat"





def question():
  x =  '{ "":""}'
  datos = input("ingresa los datos: ")
  campos = str(datos).split(",")
  com = re.findall(";$",datos)
  z = json.loads(x)
  if com:
    for cam in campos:
      y = {f"{cam}":""}
      z.update(y)
      file.append(y)
    a = json.dumps(file,indent=4)
    print(a)
  else:
    for cam in campos:
      y = {f"{cam}":""}
      z.update(y)
    question()

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






# EN ESTA FUNCION TE PIDE AMBOS ATRIBUTOS Y CAMPOS
def test():
  try:
    datos = input()
    campos = datos.split(",")
    campos = tuple(campos)
    atributos = input()
    cAtributos = atributos.split(",")
    cAtributos = tuple(cAtributos)
    w = dict(zip(campos,cAtributos))
    print(w)
    # com = re.findall(";$",datos)
  except:
    print("error alv")


test()



# EN ESTA FUNCION POR CADA CAMO QUE SE AGREGUE SE FORMARA UN ATRIBUTO VACIO
def testt():
  # try:
    datos = input("ingresa los datos: ")
    campos = datos.split(",")
    campos = tuple(campos)

    a = []
    for cam in campos:
      cam = ' '
      a.append(cam)

    a = tuple(a)
    w = dict(zip(campos,a))
    print(w)
    # com = re.findall(";$",datos)
  # except:
  #   print(NameError)

