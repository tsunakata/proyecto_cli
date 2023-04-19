from pathlib import Path

class ListaDocumentos:
    def __init__(self):
        self.files = files

    def listar(self):
        print('Estos son los documentos en carpeta: ')
        for i, file in enumerate(self.files):
            print(f"{i}) {file.name}")
        
        selection = int(input("Elige el archivo: "))
        
        try:
            index = int(selection)
            if index < 0 or index >= len(self.files):
                raise ValueError
        except ValueError:
            print('Opción incorrecta.')

        selected_file = self.files[index]
        with open(selected_file) as f:
            print(f.read())


current_path = Path.cwd()
files = list(current_path.glob('*.txt'))

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
