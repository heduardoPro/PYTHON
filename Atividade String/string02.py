import re
import textwrap

line = 'x'
result = ''
while line != '':
    if(line != ''):
        line = input()

        line = re.sub('[ ]?<hr>[ ]?', '\n'+'-'*80+'\n', line)
        result = result + line

result = textwrap.wrap(result, width=80)
for i in result:
    i = re.sub('[ ]?<br>[ ]?', '\n', i)
    print(i)