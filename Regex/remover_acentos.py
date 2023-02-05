import re

def remover_acentos(line):
    # Define as regras para substituição
    substituicoes = [
        ('á', 'a'),
        ('é', 'e'),
        ('í', 'i'),
        ('ó', 'o'),
        ('ú', 'u'),
        ('ã', 'a'),
        ('ẽ', 'e'),
        ('ĩ', 'i'),
        ('õ', 'o'),
        ('ũ', 'u'),
        ('à', 'a'),
        ('è', 'e'),
        ('ì', 'i'),
        ('ò', 'o'),
        ('ù', 'u'),
        ('â', 'a'),
        ('ê', 'e'),
        ('î', 'i'),
        ('ô', 'o'),
        ('û', 'u'),
    ]

    # Faz as substituições na string
    for original, substituicao in substituicoes:
        line = re.sub(original, substituicao, line)

    return line

texto = "Olá! meu nome é Henrique, eu não gosto de maçã."
texto_sem_acentos = remover_acentos(texto)
print(texto_sem_acentos)
