longitud = len(open('original.txt').readlines())
original = open("original.txt",'r')
linea_a_cambiar = '<dt>Madrid</dt>\n'
linea_a_cambiar_2 = '<dd>91 133 58 31</dd>\n'
cambio_1 = '<dt>Madrid <small>(Orense 69)</small></dt>\n'
cambio_2 = '<dd>91 133 58 31</dd>\n'
cambio_3 = '<dt>Madrid <small>(Arapiles 18)</small></dt>\n'
cambio_4 = '<dd>91 444 58 46 </dd>\n'

contenido = ''
diccionario = {}
for linea in range(longitud):
    line = original.readline()
    diccionario[linea] = line

print diccionario

for iteracion in range(len(diccionario)):
    try:
        file1 = diccionario[iteracion]
        file2 = diccionario[iteracion+1]
        if file1 == linea_a_cambiar and file2 == linea_a_cambiar_2:
    #if linea_a_cambiar in line and linea_a_cambiar_2 in line2:
            contenido = contenido + cambio_1 + cambio_2 + cambio_3 + cambio_4
        else:
            contenido = contenido + str(diccionario[iteracion])
    except Exception as e:
        print "error en el indice iteration"
archivo = open("modificado.txt",'w')
archivo.write(contenido)
archivo.close()
