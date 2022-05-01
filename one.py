from distutils.filelist import findall
import re, json
from sys import getsizeof
from textwrap import indent


# EN ESTA FUNCION TE PIDE AMBOS ATRIBUTOS Y CAMPOS
def test():
  try:
    empty = ()
    datos = input()
    campos = datos.split(",")
    campos = tuple(campos)
    atributos = input()
    com = re.findall(";$",atributos)
    cAtributos = atributos.split(",")
    cAtributos = tuple(cAtributos)
    if com:
      tablaDAT = dict(zip(campos,cAtributos))
      j = json.dumps(tablaDAT,indent=4)
      for item in campos:
            item = ""
            empty.__add__(item)
      tablaEST = dict(zip(campos,empty))
      jj = json.dumps(tablaEST,indent=4)
      print(j)
      print(jj)
    else:
          print("; ERROR")
  except:
    print("error alv")







campo = []

def tabla():
      Atributos = input("")
      com = re.findall(";$",str(Atributos))
      Atributos = Atributos.replace(";","")
      Latrib = Atributos.split(",")
      if len(Latrib) > 3:
            print("field error")
      else:
        campo.append(Latrib)
        if com:
          test(campo)
        else:
            tabla()



