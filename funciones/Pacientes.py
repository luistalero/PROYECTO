import funciones.globales as fg
import modules.corefilesPa as mpa
import main



def Paciente():
    title = """
*********************
* MENU DE PACIENTES *
*********************
"""
    fg.borrar_pantalla()
    print(title)
    identificacion = int(input("Ingrese el Nro de Identificacion : "))
    nombre_apellido = input('Ingrese su Nombre Completo : ')
    correo_electronico = input("Ingrese su Correo Electronico : ")
    telefono = int(input("Ingrese el Nro de Telefono : "))
    fecha_nacimiento = input('ingrese su fecha de Nacimiento : ')
    edad = int(input('Ingrese su edad : '))
    print('Masculino o Femenino')
    sexo = input("Ingrese su Genero : ")
#    r_consulta = input("Ingrese la razon de su consulta : ")
    paciente = {
        'nombre_apellido' : nombre_apellido,
        'correo_electronico' : correo_electronico,
        'telefono' : telefono,
        'fecha_nacimiento' : fecha_nacimiento,
        'edad' : edad,
        'genero' : sexo
    }
#   ool(input('Desea agregar otro Especialista S(Si) o Enter(No) : '))
#    Specialist()
    mpa.AddData('data',identificacion,paciente)
    fg.centro_Medico_CAL.get('data')
    print(f'Su numero de indentificaion es {identificacion}, Bienvenido {nombre_apellido}, su fecha de nacimento es {fecha_nacimiento} usted tiene la edad de {edad} años y su genero es {sexo}')
    if(bool(input('Desea ingresar otro paciente S(Si) o Enter(No)'))):
        Paciente(0)
    else:
        main.mainMenu(0)
    
def SearchData():
    criterio = input('Ingrese el Nro identificacion del estudiante: ')
    data=fg.centro_Medico_CAL.get('data').get(criterio)
    return data