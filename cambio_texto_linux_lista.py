#!/usr/bin/python

import os
import re
import sys
import shutil


# list of extensions to replace
#DEFAULT_REPLACE_EXTENSIONS = None
# example: uncomment next line to only replace *.c, *.h, and/or *.txt
DEFAULT_REPLACE_EXTENSIONS = (".txt")
# comprueba que los ficheros son de la extension deseada
def try_to_replace(fname, replace_extensions=DEFAULT_REPLACE_EXTENSIONS):
    if replace_extensions:
        return fname.lower().endswith(replace_extensions)
    return True

#reemplaza en el fichero seleccionado
def file_replace(fname, pat, s_after, nombre, directorio, archivo_backup, carpeta_backup):
    # first, see if the pattern is even in the file.
    # abre el fichero y pasa su contenido a contenido (string)
    with open(fname) as f:
        contenido = ''
        for linea in f:
            contenido = contenido + linea


    # pattern is in the file, so perform replace operation.
    # se define el path donde se va aguardar los archivos modificados (respetando su path)
        #save_path = 'C:\guardados'
        # el path completo se forma con el path de guardado y el path del archivo menos C:
        completeName = os.path.join(directorio, nombre)
        # si no existe el directorio en el directorio destino se crea
        #d = os.path.dirname(completeName)
        #if not os.path.exists(d):
        #    os.makedirs(d)
        # Se escribe el nuevo fichero
        out = open(completeName, "w")
        # se reemplaza el texto en base a las variables proporcionadas
        new_data = contenido.replace(find_str, replace_str)
        # se escribe el nuevo fichero con las modificaciones
        out.write(new_data)
        out.close()
        # se compara el tamano del archivo original y el modificado
        fichero_moderno_size = os.path.getsize(completeName)
        fichero_antiguo_size = os.path.getsize(archivo_backup)
        # si el tamano ha cambiado se escribe en la lista de cambios
        if fichero_moderno_size != fichero_antiguo_size:
            lista_archivos_modificados = open(carpeta_backup+"/lista.txt", 'a')
            lista_archivos_modificados.write(str(completeName+'\n'))
            lista_archivos_modificados.close()
        else:
            # si el tamano no ha cambiado se borra el archivo del backup
            os.remove(archivo_backup)



        #os.rename(out_fname, fname)


def mass_replace(dir_name, s_before, s_after, replace_extensions=DEFAULT_REPLACE_EXTENSIONS):
    #pat = re.compile(s_before)
    carpeta_backup = "/home/cepal/backup"
    lista_archivos_modificados = open(carpeta_backup+"/lista.txt", 'w')
    lista_archivos_modificados.close()
    pat = s_before
    # se recorre el directorio de trabajo proporcionado
    for dirpath, dirnames, filenames in os.walk(dir_name):
        # se recorren los archivos en cada directorio
        for fname in filenames:
            # se comprueba si el archivo tiene la extension que requerimos
            if try_to_replace(fname, replace_extensions):
                fullname = os.path.join(dirpath, fname)

                archivo_backup = carpeta_backup + fullname
                check = os.path.dirname(archivo_backup)
                if not os.path.exists(check):
                    os.makedirs(check)


                shutil.copyfile(fullname,archivo_backup )
                file_replace(fullname, pat, s_after,fname, dirpath, archivo_backup, carpeta_backup)

find = open("buscar.txt", 'r')
replace = open("reemplazar.txt", 'r')


find_str = ""
replace_str = ""



for line in find: # concatenate it into one long string
    find_str += line

for line in replace:
    replace_str += line
print find_str
print replace_str

mass_replace("/home/cepal/originales", find_str, replace_str)
