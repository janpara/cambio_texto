import re

data = open("original.txt", 'r')
find = open("buscar.txt", 'r')
replace = open("reemplazar.txt", 'r')

data_str = ""
find_str = ""
replace_str = "" 

for line in data: # concatenate it into one long string
    data_str += line

for line in find: # concatenate it into one long string
    find_str += line

for line in replace: 
    replace_str += line
print data_str
print find_str
print replace_str



new_data = data_str.replace(find_str, replace_str)
new_file = open("new_data.txt", "w")
new_file.write(new_data)
new_file.close()
