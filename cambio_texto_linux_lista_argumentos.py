#!/usr/bin/python
# operaciones con directorios
import os
# pasar argumentos desde consola
import sys
# copiar ficheros
import shutil
# obtener la fecha actual
import time

#variables globales

CARPETA_BACKUP = "/home/cepal/backup/"
fecha_de_backup = time.strftime("%d_%m_%Y")
ruta_completa_carpeta_backup = CARPETA_BACKUP + fecha_de_backup + "/"
# list of extensions to replace
# descomentar la siguiente linea si no se quiere filtrar por extension
#DEFAULT_REPLACE_EXTENSIONS = None
# actualmente solo se trabaja en los archivos con extension .html
DEFAULT_REPLACE_EXTENSIONS = (".html")
# comprueba que los ficheros son de la extension deseada
def try_to_replace(fname, replace_extensions = DEFAULT_REPLACE_EXTENSIONS):
    if replace_extensions:
        return fname.lower().endswith(replace_extensions)
    return True

#reemplaza en el fichero seleccionado
# se le pasan los siguientes parametros:
# fname - ruta completa del archivo origen
# archivo_backup - ruta completo del archivo de backup (original sin modificar)
def file_replace(fname, archivo_backup):

    # first, see if the pattern is even in the file.
    # abre el fichero y pasa su contenido a contenido (string)
    with open(fname) as f:
        contenido = ''
        for linea in f:
            contenido += linea


        # pattern is in the file, so perform replace operation.
        # Se escribe el nuevo fichero
        out = open(fname, "w")
        # se reemplaza el texto en base a las variables proporcionadas
        new_data = contenido.replace(TEXTO_A_BUSCAR, TEXTO_A_REEMPLAZAR)
        # se escribe el nuevo fichero con las modificaciones
        out.write(new_data)
        out.close()
        # se compara el tamano del archivo original y el modificado
        fichero_moderno_size = os.path.getsize(fname)
        fichero_antiguo_size = os.path.getsize(archivo_backup)
        # si el tamano ha cambiado se escribe en la lista de cambios
        if fichero_moderno_size != fichero_antiguo_size:
            lista_archivos_modificados = open(ruta_completa_carpeta_backup  + fecha_de_backup + ".txt" , 'a')
            lista_archivos_modificados.write(str(fname+'\n'))
            lista_archivos_modificados.close()
        else:
            # si el tamano no ha cambiado se borra el archivo del backup
            os.remove(archivo_backup)

# se le pasan los siguientes parametros:
# directorio_de_trabajo - el directorio que se va a explorar para buscar los archivos a modificar
# replace_extensions - Las extensiones que se consideraran a la hora de modificar archivos

def mass_replace(directorio_de_trabajo, replace_extensions=DEFAULT_REPLACE_EXTENSIONS):
    check = os.path.dirname(ruta_completa_carpeta_backup)
    if not os.path.exists(check):
        # si no existe se crea
        os.makedirs(check)
        print "se crea la carpeta de backup en la siguiente ruta:" + ruta_completa_carpeta_backup
    else:
        print " la ruta de backup ya existe. Especifica otra ruta para no sobreescribir datos"
        return
    lista_archivos_modificados = open(ruta_completa_carpeta_backup  + fecha_de_backup + ".txt", 'w')
    lista_archivos_modificados.close()
    # se recorre el directorio de trabajo proporcionado
    for dirpath, dirnames, filenames in os.walk(directorio_de_trabajo):
        # se recorren los archivos en cada directorio
        for fname in filenames:
            # se comprueba si el archivo tiene la extension que requerimos
            if try_to_replace(fname, replace_extensions):
                ruta_completa_texto_original = os.path.join(dirpath, fname)

                ruta_completa_archivo_backup = ruta_completa_carpeta_backup + ruta_completa_texto_original
                # se comprueba si existe el directorio en la carpeta de backup
                check = os.path.dirname(ruta_completa_archivo_backup)
                if not os.path.exists(check):
                    # si no existe se crea
                    os.makedirs(check)

                #se copia el archivo original a la carpeta de backup
                shutil.copyfile(ruta_completa_texto_original,ruta_completa_archivo_backup )
                # Se llama al metodo para reemplazar el texto
                file_replace(ruta_completa_texto_original, ruta_completa_archivo_backup)

# Se abren los ficheros donde se encuentran los patrones a buscar y reemplazar
find = open("buscar.txt", 'r')
replace = open("reemplazar.txt", 'r')


TEXTO_A_BUSCAR = ""
TEXTO_A_REEMPLAZAR = ""


# Se genera variables string con los patrones de busqueda y reemplazo
for line in find: # concatenate it into one long string
    TEXTO_A_BUSCAR += line

for line in replace:
    TEXTO_A_REEMPLAZAR += line

# se llama al metodo principal del programa con el directorio de trabajo a examinar
mass_replace("/home/cepal/originales")

