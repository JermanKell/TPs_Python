import xml.etree.ElementTree as ET
import sqlite3
import makedatabase

def impdatabase(nom_xml, nom_db):
    makedatabase.create_database(nom_db)
    conn = sqlite3.connect(nom_db)
    c = conn.cursor()

    tree = ET.parse(nom_xml)
    root = tree.getroot()

    #COMMUNES
    for children in root.iter('communes'):
        c.execute("insert into Communes values (?, ?, ?, ?)",
                  (children.find('code_dpt').text, children.find('code_com').text, children.find('nom_com').text, int(children.find('pop_tot').text)))

    #DEPARTEMENTS
    for children in root.iter('repartements'):
        c.execute("insert into Departements values (?, ?, ?)",
                  (children.find('code_dpt').text, children.find('nom_dpt').text, children.find('code_reg').text))

    #REGION
    for children in root.iter('region'):
        c.execute("insert into Region values (?, ?)",
                  (children.find('code_reg').text, children.find('nom_reg').text))

    conn.commit()
    conn.close()