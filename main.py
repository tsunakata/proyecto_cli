from pathlib import Path
from listar import ListaDocumentos

while True:
    print('Bienvenido. ¿Listar documentos?')
    print('1) Sí.')
    print('2) No.')

    choice = int(input("Escribe una opción: "))

    if choice == 1:
        listar = ListaDocumentos()
        listar.listar()
    elif choice == 2:
        print('El programa se detendrá.')
        break
    else:
        print('Opción incorrecta.')
