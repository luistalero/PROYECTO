import os
import json
import funciones.globales as fg
import modules.corefilesEs as cf
import ui.uiEspecialistas as uiS
import main
def Specialist():
    title = """
    **********************
    * NUEVO ESPECIALISTA *
    **********************
    """
    fg.borrar_pantalla()
    print(title)
    identificacion = int(input("Ingrese el Nro de Identificacion : "))
    print('Tenga en cuenta que las especializaciones con las que contamos son :')
    print('Pediatría-Ginecología-Dermatología-Endocrinología-Optometría')
    especializacion = input("Ingrese su Especializacion : ")
    nombre_apellido = input('Ingrese su Nombre Completo : ')
    correo_electronico = input("Ingrese su Correo Electronico : ")
    telefono = int(input("Ingrese el Nro de Telefono : "))
    consultorio = int(input("Ingrese el numero de su consultorio : "))
    print('los horarios se dividen en M(Mañana) o T(Tarde)')
    horario = input("Ingrese su Horario de Atencion : ")
    Especialista = {
        'especialista' : especializacion,
        'nombre_apellido' : nombre_apellido,
        'correo_electronico' : correo_electronico,
        'telefono' : telefono,
        'consultorio' : consultorio,
        'horario' : horario
    }
#   ool(input('Desea agregar otro Especialista S(Si) o Enter(No) : '))
#    Specialist()
    cf.AddData('data_especialistas',identificacion,Especialista)
    fg.centro_Medico_CAL.get('data_especialistas')
    print(f'Su numero de indentificaion es {identificacion}, Bienvenido {nombre_apellido}, El consultorio que se te asigno fue {consultorio} y trabajas en la jornada {horario}')
    if(bool(input('Desea ingresar otro especialista S(Si) o Enter(No)'))):
        Specialist()
    else:
        main.mainMenu(0)
    
def SearchData():
    criterio = int(input('Ingrese el Nro identificacion del especialista: '))
    data = fg.centro_Medico_CAL.get('data_especialistas')
    return data

def ModifyData():
    dataespecialist = SearchData()
    correo_electronico,telefono,consultorio,horario = dataespecialist.values()
    for key in dataespecialist.key():
        if (key != 'identificacion' and key != 'especializacion'):
            if(bool(input(f'Desea modificar el {key} S(si) o Enter(No)'))):
                dataespecialist[key] = input(f'Ingrese el nuevo valor para {key} :')
    fg.centro_Medico_CAL.get('data_especialistas').update({correo_electronico:dataespecialist})
    cf.UpdateFile(fg.centro_Medico_CAL)
    uiS.NewEspecialist(0)