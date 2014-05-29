longitud = len(open('original.txt').readlines())
original = open("original.txt",'r')
linea_a_cambiar = '<dt>Madrid</dt>'
linea_a_cambiar_2 = '<dd>91 133 58 31</dd>'
cambio_1 = '<dt>Madrid <small>(Orense 69)</small></dt>\n'
cambio_2 = '<dd>91 133 58 31</dd>\n'
cambio_3 = '<dt>Madrid <small>(Arapiles 18)</small></dt>\n'
cambio_4 = '<dd>91 444 58 46 </dd>\n'

contenido = ''

for linea in original:

    line2 = original.next()
    if linea_a_cambiar in linea and linea_a_cambiar_2 in line2:
        contenido = contenido + cambio_1 + cambio_2 + cambio_3 + cambio_4

    else:
        contenido = contenido + linea

archivo = open("modificado.txt",'w')
archivo.write(contenido)
archivo.close()



