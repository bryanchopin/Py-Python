import re, json
# datos = input("ingresa los datos: ").split(',')
# com = re.findall(";$",datos)
# print(com)


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
    j = json.dumps(w,indent=4)
    print(j)
    # com = re.findall(";$",datos)
  except:
    print("error alv")


test()