import sys,re

# x='si'

# while x=='si':
#     tecla = sys.stdin.read(1)
#     if tecla == ';':
#         print ('Has presionado ', tecla)
#     else:
#         x='si'
#         print ('Se rompe el bucle')


txt =input('insert the intruction: ')

#Check if the string ends with 'planet':

x = re.findall(";$", txt)
if x:
  print(f"ends with ;")
else:
  print("No match")


def crearDB():
    try:
        directory = input("Crea base ")
        com = re.findall(";$",directory)
        if com:
            path = os.path.join(parent_dir, directory)
            os.mkdir(path)
    except OSError:
        print("DB created fail")
    else:
        print("DB created successfully")