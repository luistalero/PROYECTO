import funciones.globales as fg
import funciones.Pacientes as fp
import modules.corefilesPa as mc
import main

def NewPacient(op : int):
    fg.borrar_pantalla()
    title = """
*****************
* MENU DE CITAS *
*****************
"""
    NewPacientOP = "1. Paciente nuevo\n2. Paciente antiguo\n3. salir"
    if (op != 3):
        print(title)
        print(NewPacientOP)
        try:
            op = int(input(':) '))
        except ValueError:
            print("Error en la opcion ingresada")
            fg.pausar_pantalla()
            NewPacient(0)
        else:
            match (op):
                case 1:
                    fp.Paciente()
                case 2:
                    print('Estoy trabajando en esto....')
                    fg.pausar_pantalla()
                    NewPacient(0)
                case 3:
                    print("Regresando al menu anterior ")
                    fg.pausar_pantalla()
                    main.mainMenu(0)
                case _:
                    print('La opcion ingresada no es valida')
                    input('Precione Enter para continuar.... ')
                    fg.pausar_pantalla