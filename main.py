from pathlib import Path
current_path = Path.cwd()
print(current_path)

while True:
    print("Menú: ")
    print("1) Listar documentos.")
    print("2) Leer documento.")
    print("3) Eliminar documento.")
    print("4) Salir.")

    choice = int(input("Escribe una opción: "))

    if choice == 1:
        for file in current_path.iterdir():
            if file.is_file():
                print(file.name)
    elif choice == 2:
        print("Leer documento.")
    elif choice == 3:
        print("Eliminar documento.")
    elif choice == 4:
        break
    else:
        print("Opción incorrecta.")
