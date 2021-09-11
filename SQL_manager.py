import sqlite3


def SQL_operations(operation, adress, latit, longit):
    # conn = connection
    conn = sqlite3.connect('teste_sancathon.sqlite')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Location (adress TEXT, lat REAL, long REAL)'''
    )

    if operation.upper() == 'INSERT':
        cursor.execute('INSERT INTO Location (adress, lat, long) VALUES (?, ?, ?)', (adress, latit, longit))
    if operation.upper() == 'DELETE':
        cursor.execute('DELETE FROM Location WHERE adress=?', (adress,))

    conn.commit()


def main():

    while(True):
        operation = input("Operation: ")
        adress = input("Adress: ")
        latitude = float(input("Latitude: "))
        longitude = float(input("Longitude: "))

        SQL_operations(operation, adress, latitude, longitude)


if __name__ == '__main__':
    main()