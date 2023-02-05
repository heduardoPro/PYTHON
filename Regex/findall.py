import re
from rich import print
str = 'purple alice@google.com, blah monkey bob_a@abc.com blah dishwasher, azevedo.henrique1@ifrn.edu.br'

emails = re.findall('([a-z0-9_.+-]+@[a-z]+\.[a-z.]+)', str)
print('[red]Emails: ', emails)