import re

telefones = "81 91234-1234, 81 91234 1234, 81 912341234, 84999999999, (81) 9 9898-9898, (81) 9 8787 8787, (81)912345678, 123.456.789-10"

new_telefones = re.findall('\(?[0-9]{2}.*9[0-9]{4}[- ]?[0-9]{4}', telefones)
print('telefones validos: ', new_telefones)

no_telefones = re.search('([0-9]{3}\.){2}[0-9]{3}\-[0-9]{2}', telefones)
print('outros: ', no_telefones)