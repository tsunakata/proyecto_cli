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

        while True:
            print('¿Qué deseas hacer con el documento?')
            print('1) Abrir.')
            print('2) Editar.')
            print('3) Eliminar.')
            print('4) Regresar al menú principal.')

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
                while True:
                    print('¿Estás seguro de eliminar el archivo?')
                    print('1) Sí.')
                    print('2) No.')
                    third_selection = int(input("Elige la opción: "))

                    if third_selection == 1:
                        selected_file.unlink()
                        print('Archivo borrado.')
                        break
                    elif third_selection == 2:
                        break
                    else:
                        print('Opción incorrecta.')
            elif second_selection == 4:
                break
            else:
                print('Opción incorrecta.')


current_path = Path.cwd()
files = list(current_path.glob('*.txt'))