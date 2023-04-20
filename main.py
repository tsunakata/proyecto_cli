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

        print('¿Qué deseas hacer con el documento?')
        print('1) Abrir.')
        print('2) Editar.')
        print('3) Eliminar.')

        second_selection = int(input("Elige la opción: "))
        selected_file = self.files[index]

        if second_selection == 1:
            with open(selected_file) as f:
                print(f.read())
        elif second_selection == 2:
            text = input('Ingresa el texto a añadir: ')
            with open(selected_file, 'a+') as f:
                print(f.write('\n' + text))
        elif second_selection == 3:
            pass
        else:
            print('Opción incorrecta.')


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
