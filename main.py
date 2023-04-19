from pathlib import Path
current_path = Path.cwd()
files = list(current_path.glob('*.txt'))

while True:
    print('Bienvenido. ¿Listar documentos?')
    print('1) Sí.')
    print('2) No.')

    choice = int(input("Escribe una opción: "))

    if choice == 1:
        print('Estos son los documentos en carpeta: ')
        for i, file in enumerate(files):
            print(f"{i}) {file.name}")
    elif choice == 2:
        print('El programa se detendrá.')
        break
    else:
        print('Opción incorrecta.')
"""
while True:
    print("Menú: ")
    print("1) Listar documentos.")
    print("2) Leer documento.")
    print("3) Eliminar documento.")
    print("4) Salir.")

    choice = int(input("Escribe una opción: "))

    if choice == 1:
        for i, file in enumerate(files):
            print(f"{i}, {file.name}")
    elif choice == 2:
        print("Leer documento.")
    elif choice == 3:
        print("Eliminar documento.")
    elif choice == 4:
        break
    else:
        print("Opción incorrecta.")
"""