import sqlite3

def SQL_operations_Location(table, operation, adress, latit, longit):
    # conn = connection
    conn = sqlite3.connect('teste_sancathon.sqlite')
    cursor = conn.cursor()
    
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {table} (adress TEXT, lat REAL, long REAL)''', 
    )

    if operation.upper() == 'INSERT':
        cursor.execute('INSERT INTO Location (adress, lat, long) VALUES (?, ?, ?)', (adress, latit, longit))
        print("OPERAÇÃO BEM SUCEDIDA")
    if operation.upper() == 'DELETE':
        cursor.execute('DELETE FROM Location WHERE adress=?', (adress,))
        print("OPERAÇÃO BEM SUCEDIDA")

    conn.commit()

def SQL_operations_Lines(table, operation, weight, dpdb, dpdt):
    # conn = connection
    conn = sqlite3.connect('teste_sancathon.sqlite')
    cursor = conn.cursor()

    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {table} (weight REAL, dpdb REAL, dpdt REAL)''',     
    )

    if operation.upper() == 'INSERT':
        cursor.execute(f'''
            INSERT INTO {table} (weight, dpdb, dpdt) 
            VALUES (?, ?, ?)''', (weight, dpdb, dpdt)
        )
    if operation.upper() == 'DELETE':        
        cursor.execute(f'''
            DELETE FROM {table} WHERE weight=?''', (weight, )
        )
    
    conn.commit()
    print("OPERAÇÃO BEM SUCEDIDA")

def main():

    print('''Bem vindo ao gerenciador do banco de dados SQL GRABus
Uma descrição breve dos parametros básicos:
        1. table: A tabela "Location" refere a tabela com as coordenadas dos
        pontos, para referencair as linhas deve se por "Linha" + numero da linha
        2. Operation: Operação a ser feito no banco de dados (inserção, Remoção e etc)
        ''')

    while(True):
        table = input("Table: ")
        operation = input("Operation: ")
        if table == "Location":
            adress = input("Adress: ")
            latitude = float(input("Latitude: "))
            longitude = float(input("Longitude: "))
            SQL_operations_Location(table, operation, adress, latitude, longitude)
        else:
            weight = float(input("Weight: "))
            dpdb = float(input("People flow per bus: "))
            dpdt = float(input("People flow per time: "))
            SQL_operations_Lines(table, operation, weight, dpdb, dpdt)



if __name__ == '__main__':
    main()