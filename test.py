import json,re

from main import test






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