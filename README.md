# PROYECTO MASTER

## Descripción
Este proyecto es un sistema de gestión de pacientes y especialistas, desarrollado en Python. Permite manejar información sobre especialistas y pacientes mediante archivos JSON, con una estructura modular organizada para facilitar su mantenimiento y escalabilidad.

## Estructura del Proyecto

- `main.py`: Archivo principal que ejecuta el programa.
- `config.py`: Archivo de configuración con rutas y opciones generales.
- `data/`: Contiene los archivos JSON con la información de los especialistas y pacientes.
  - `especialistas.json`: Datos de los especialistas.
  - `pacientes.json`: Datos de los pacientes.
- `funciones/`: Contiene funciones auxiliares para manejar la lógica del programa.
  - `gestor_datos.py`: Funciones para cargar y guardar datos en JSON.
  - `Especialistas.py`: Funciones relacionadas con los especialistas.
  - `Pacientes.py`: Funciones relacionadas con los pacientes.
- `modules/`: Contiene módulos adicionales de soporte.
  - `corefilesEs.py`: Funcionalidades relacionadas con especialistas.
  - `corefilesPa.py`: Funcionalidades relacionadas con pacientes.
- `ui/`: Contiene la interfaz de usuario para especialistas y pacientes.
  - `main_ui.py`: Archivo principal de UI.
  - `views/`: Carpeta con vistas separadas.
    - `especialistas.py`: Interfaz para gestionar especialistas.
    - `pacientes.py`: Interfaz para gestionar pacientes.
- `.vscode/launch.json`: Configuración para depuración en Visual Studio Code.
- `.gitignore`: Archivo para excluir cachés y archivos innecesarios.

## Instalación y Ejecución

### Requisitos Previos
- Python 3.12 o superior
- Librerías necesarias (si es necesario, instalar con `pip`)

### Pasos para ejecutar el proyecto
1. Clonar o descargar el repositorio.
2. Abrir una terminal en la carpeta del proyecto.
3. Ejecutar el siguiente comando:
   ```bash
   python main.py
   ```
## Contacto
- **Creador**: [Talero_Luis]
- **Correo Electrónico**: [luisalbertotaleromartinez@gmail.com]
- **GitHub**: [https://github.com/luitalero](https://github.com/luistalero)
