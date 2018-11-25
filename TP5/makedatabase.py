import sqlite3

def create_database(nom_db):
    conn = sqlite3.connect(nom_db)
    c = conn.cursor()

    c.execute('''CREATE TABLE if not exists Communes
                 (code_dpt text, code_com text, nom_com text, pop_tot integer)''')

    c.execute('''CREATE TABLE if not exists Departements
                 (code_dpt text, nom_dpt text, code_reg text)''')

    c.execute('''CREATE TABLE if not exists Region
                 (code_reg text, nom_reg text)''')
    conn.commit()
    conn.close()

def fill_database(nom_db):
    conn = sqlite3.connect(nom_db)
    c = conn.cursor()

    file_name = '''bdd/communes.csv'''
    file = open(file_name, "rt")
    file_content = file.read()
    file_content = file_content.split("\n")

    del file_content[0:8]
    del file_content[len(file_content)-1]

    for line in file_content:
        if len(line) > 0:
            data_array = line.split(";")
            if len(data_array[0]) > 0:
                c.execute("insert into Communes values (?, ?, ?, ?)", (data_array[2], data_array[5], data_array[6], int(data_array[9].replace(" ", ""))))
    file.close()

    file_name = '''bdd/departements.csv'''
    file = open(file_name, "rt")
    file_content = file.read()
    file_content = file_content.split("\n")

    del file_content[0:8]
    del file_content[len(file_content)-1]

    for line in file_content:
        if len(line) > 0:
            data_array = line.split(";")
            if len(data_array[0]) > 0:
                c.execute("insert into Departements values (?, ?, ?)", (data_array[2], data_array[3], data_array[1]))
    file.close()

    file_name = '''bdd/departements.csv'''
    file = open(file_name, "rt")
    file_content = file.read()
    file_content = file_content.split("\n")

    del file_content[0:8]
    del file_content[len(file_content)-1]

    for line in file_content:
        if len(line) > 0:
            data_array = line.split(";")
            if len(data_array[0]) > 0:
                c.execute("insert into Region values (?, ?)", (data_array[0], data_array[1]))
    file.close()

    conn.commit()
    conn.close()

def sum_total_pop_department():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT code_dpt, SUM(pop_tot) FROM Communes GROUP BY code_dpt')
    for row in c:
        print(row)
    c.close()
    conn.close()

def sum_total_pop_region():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT code_reg, SUM(pop_tot) FROM Communes INNER JOIN Departements on Departements.code_dpt = Communes.code_dpt GROUP BY code_reg')
    for row in c:
        print(row)
    c.close()
    conn.close()

def list_department_com():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT nom_com, code_dpt FROM Communes WHERE nom_com IN (SELECT nom_com FROM Communes GROUP BY nom_com HAVING COUNT(*) > 1) ORDER BY nom_com ASC')
    for row in c:
        print(row)
    c.close()
    conn.close()

def modify_database(nom_db):
    conn = sqlite3.connect(nom_db)
    c = conn.cursor()
    c.execute('''CREATE TABLE if not exists NouvellesRegions
                 (code_nouv_reg integer, lib_geo text)''')

    file_name = '''bdd/zones-2016.csv'''
    file = open(file_name, "rt")
    file_content = file.read()
    file_content = file_content.split("\n")

    #Récupère uniquement les lignes REG du fichier
    for line in file_content:
        if len(line) > 0:
            data_array = line.split(";")
            if len(data_array[0]) > 0:
                if data_array[0].__eq__('REG'):
                    print(data_array[1], data_array[2])
                    c.execute("insert into NouvellesRegions values (?, ?)", (data_array[1], data_array[2]))
    file.close()

    c.execute('ALTER TABLE Departements ADD COLUMN code_nouv_reg interger')
    file_name = '''bdd/communes-2016.csv'''

    file = open(file_name, "rt")
    file_content = file.read()
    file_content = file_content.split("\n")

    del file_content[0:7]

    departements_updated = []
    for line in file_content:
        if len(line) > 0:
            data_array = line.split(";")
            if len(data_array[0]) > 0:
                if not data_array[2] in departements_updated:
                    c.execute('update Departements set code_nouv_reg = ' + data_array[3] + ' where code_dpt = \'' + data_array[2] + '\'')
                    departements_updated.append(data_array[2])
    file.close()

    conn.commit()
    conn.close()

def new_sum_pop():
    conn = sqlite3.connect('database2.db')
    c = conn.cursor()
    c.execute('SELECT NouvellesRegions.code_nouv_reg, lib_geo, SUM(pop_tot) FROM NouvellesRegions '
              'INNER JOIN Departements on Departements.code_nouv_reg = NouvellesRegions.code_nouv_reg '
              'INNER JOIN Communes on Communes.code_dpt = Departements.code_dpt GROUP BY NouvellesRegions.code_nouv_reg')
    for row in c:
        print(row)
    c.close()
    conn.close()
