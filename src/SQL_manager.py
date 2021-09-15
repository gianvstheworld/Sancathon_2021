''' Conjunto de códigos desenvolvidos para o Sancathon 2021
                                > GRABus < 

* Código de manejamento do banco de dados de SQL:
    O objetivo do desenvolvimento desse projeto em python era mostrar a viabilidade de 
se trabalhar com banco de dados SQL para armazenar os dados vindos das diversas redes de
obtenção de dados sobre tanto os pontos de onibus quanto as linhas. É válido lembrar que 
todos os códigos do projeot são versões betas que podem ser aperfeiçoados e mais explorados
em outros escopos fora do Sancathon.
    Uma das principais motivações de se trabalhar com SQL é a viabilização de utilizar um 
banco de dados do tamanho necessário para alimentar as outras componentes do projeto. Por
meio desse código de manutenção do banco de dados seria possível inserir e deletar 
(obviamente em uma versão completa do projeto novas funções estariam implementadas) de
forma fácil e eficiente computacioalmente falando. 
    A motivação de utilziar a lingaugem python para fazer a ponte com o banco de dados foi
a facilidade, uma vez que entedemos que a maioria dos usuarios do programa (funcionarios de
empresas ou de orgãos publicos) estariam mais ligados com a área de mobilidade urbana e 
não possuiriam um amplo conhecimento de em desenvolvimento e computação. Assim, o python 
ofereceria umaa linguagem em alto nivel com alta facildiade para os usuarios e para os 
desevolvedores.
    Por fim, optamos pela escolha do SQLite pela facilidade de implementação novamente e 
por ser um programa open source disponiveis para todos acessarem o projeto e realizar seus
próprios teste. Em um cenário no qual o projeto sairia  do beta seria necessário um SQL 
manager mais robusto, uma boa opção é o MySQL, Oracle SQL ou o Microsoft SQL Server, todos
possuem as funções necessárias parao o desenvolvimento do projeto e para a quantidade de dados
que espera-se trabalhar, porém não são open source e possuem um custo de uso.

'''

import sqlite3

# Função que opera com a tabela do banco de dados dos pontos de onibus
def SQL_operations_Location(table, operation, adress, latit, longit):
    
    # conn = connection, representa conexão com o banco de dados local na maquina 
    conn = sqlite3.connect('GRABus.sqlite')
    # cursor para gerenciamento do banco de daods aberto
    cursor = conn.cursor()
    
    # executa o comando no banco de dados criando a tabela com o nome pedido e com os 
    # parametros para uma localização
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {table} (adress TEXT, lat REAL, long REAL)''', 
    )

    # Por enquanto apenas duas operações foram implementadas: Inserção e Remoção
    if operation.upper() == 'INSERT':
        cursor.execute('''
            INSERT INTO Location (adress, lat, long) 
            VALUES (?, ?, ?)''', (adress, latit, longit)
        )
    if operation.upper() == 'DELETE':
        cursor.execute('''
            DELETE FROM Location 
            WHERE adress=?''', (adress,)
        )

    # Confirma as operações feitas no banco de dados
    conn.commit()
    print("OPERAÇÃO BEM SUCEDIDA")

# Função que opera com a tabela do banco de dados dos pontos de onibus
def SQL_operations_Lines(table, operation, weight, dpdb, dpdt):
    
    # conn = connection, representa conexão com o banco de dados local na maquina 
    conn = sqlite3.connect('GRABus.sqlite')
    # cursor para gerenciamento do banco de daods aberto
    cursor = conn.cursor()
    
    # executa o comando no banco de dados criando a tabela com o nome pedido e com os 
    # parametros para uma linha
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {table} (weight REAL, dpdb REAL, dpdt REAL)''',     
    )

    # Por enquanto apenas duas operações foram implementadas: Inserção e Remoção
    if operation.upper() == 'INSERT':
        cursor.execute(f'''
            INSERT INTO {table} (weight, dpdb, dpdt) 
            VALUES (?, ?, ?)''', (weight, dpdb, dpdt)
        )
    if operation.upper() == 'DELETE':        
        cursor.execute(f'''
            DELETE FROM {table} WHERE weight=?''', (weight, )
        )
    
    # Confirma as operações feitas no banco de dados
    conn.commit()
    print("OPERAÇÃO BEM SUCEDIDA")

def main():

    # Descrição breve para o usuário
    print('''Bem vindo ao gerenciador do banco de dados SQL GRABus
Uma descrição breve dos parametros básicos:
        1. table: A tabela "Location" refere a tabela com as coordenadas dos
        pontos, para referencair as linhas deve se por "Linha" + numero da linha
        2. Operation: Operação a ser feito no banco de dados (inserção, Remoção e etc)
        ''')

    # looping para permitir que o usuario faça varias operações facilmente
    while(True):
        # inputs
        table = input("Table: ")
        operation = input("Operation: ")
        # caso para a operação na tabela de ponto de onibus
        if table == "Location":
            adress = input("Adress: ")
            latitude = float(input("Latitude: "))
            longitude = float(input("Longitude: "))
            SQL_operations_Location(table, operation, adress, latitude, longitude)
        # caso para a operação em outras tabelas, como a de cada linha em especifico
        else:
            weight = float(input("Weight: "))
            dpdb = float(input("People flow per bus: "))
            dpdt = float(input("People flow per time: "))
            SQL_operations_Lines(table, operation, weight, dpdb, dpdt)

# Invoca a função main
if __name__ == '__main__':
    main()

