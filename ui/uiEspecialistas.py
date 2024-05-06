import funciones.globales as fg
#import modules.corefilesEs as mce
import funciones.Especialistas as fe
import main


def NewEspecialist(op : int):
    title = """
***********************
* MENU ADMINISTRATIVO *
***********************
    """

    NewEspecialistOp = "1. Añadir Especialista \n2. Editar Especialista\n3. Borrar Especialista\n4. Salir"
    fg.borrar_pantalla()
    if (op != 4):
        print(title)
        print(NewEspecialistOp)
        try:
            op = int(input(':) '))
        except ValueError:
            print("Error en la opcion ingresada")
            fg.pausar_pantalla()
            NewEspecialist(0)
        else:
            match (op):
                case 1:
                    fe.Specialist()
                case 2:
                    fe.ModifyData()
                case 3:
                    #fe.delete()
                    print('Estoy trabajando en esto...')
                    fg.pausar_pantalla()
                    NewEspecialist(0)
                case 4:
                    print("Regresando al menu anterior ")
                    fg.pausar_pantalla()
                    main.mainMenu(0)
                case _:
                    print('La opcion ingresada no es valida')
                    fg.pausar_pantalla()