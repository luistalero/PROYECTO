import modules.corefilesEs as mce
import modules.corefilesPa as Mpa
import funciones.globales as fg
import funciones.Pacientes as fp
import ui.uiEspecialistas as uiS
import ui.uiPacientes as uiP
import funciones.Especialistas as fe
def mainMenu(op):
    fg.borrar_pantalla()
    title = """
********************************************************
* MENU PRINCIPAL DEL CENTRO MEDICO CARLOS ARDILA LÜLLE *
********************************************************
    """
    mainMenuOp = "1. Admin Especialistas \n2. Apartar Cita \n3. Consultar cita \n4. Salir"
    if(op != 4):
        print(title)
        print(mainMenuOp)
        try:
            opcion = int(input(':) '))
        except ValueError:
            print("Error en la opcion ingresada")
            fg.pausar_pantalla()
            mainMenu(0)
        else:
            match (opcion):
                case 1:
                    uiS.NewEspecialist(0)
                case 2:
                    uiP.NewPacient(0)
                case 3:
                    print('Estoy trabajando en esto...')
                    fg.pausar_pantalla( )
                    mainMenu(0)
                case 4:
                    print("Regrese pronto ....")
                    fg.pausar_pantalla
                case _:
                    print('Opcion ingresada no pertenece al menu de opciones')
                    fg.pausar_pantalla()
                    mainMenu(0)
if __name__ == '__main__':
    Mpa.MY_DATABASE = 'data/pacientes.json'
    mce.MY_DATABASE = 'data/especialistas.json'
    Mpa.checkFile(fg.centro_Medico_Cal)
    mce.checkFile(fg.centro_Medico_CAL)
    mainMenu(0)