import re

txt = input()

for i in range(0, int(txt)):
    line = input()

    if(re.search('\d', line)):
        
        line = re.sub('[Oo]', '0', line)
        line = re.sub('l', '1', line)
        line = re.sub(',| ', '', line)
        line = re.sub('^0+0$', '0', line) 

        if(int(line) < 0 or int(line) > 2147483647):
            print('error')
        else:
            print(line)
    else:
        print('error')