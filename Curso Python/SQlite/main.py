import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

conection = sqlite3.connect(DB_FILE) #fazendo conexão do sqlite3 com o arquivo
cursor = conection.cursor() #create cursor 

#CUIDADO: fazendo delete sem where
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)
#DELETANTO a sequencia, e iniciando o ID do inicio
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
conection.commit()

#CRIA A TABELA
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,' #id-CHAVE PRIMARIA DA TABELA e INCREMENTA QUANDO FOR INSERIR ALGO NA BASE DE DADOS
    'name TEXT,'
    'weight REAL'
    ')'
)
conection.commit()

#INSERIR DADOS NAS COLUNAS DA TABELA
'''
cursor.execute(
    f'INSERT INTO {TABLE_NAME} (id, name, weight) '
    'VALUES (NULL, "Henrique", 10), (NULL, "Maria", 18), (NULL, "Test", 0.0)'
)
'''
cursor.execute(
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight) '
    'VALUES '
    '(?, ?)' #BINDINGS
    )
#CRUD - CREATE READ UPDATE DELETE
#SQL -  INSERT SELECT UPDATE DELETE

conection.commit()

cursor.close()
conection.close()
