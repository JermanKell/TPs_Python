import xml.etree.cElementTree as ET
import sqlite3

def expdatabase(nom_xml):
    XMLdatabase = ET.Element("database")
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    #COMMUNES
    c.execute('SELECT code_dpt, code_com, nom_com, pop_tot FROM Communes')
    for row in c:
        XMLcommunes = ET.SubElement(XMLdatabase, "communes")
        ET.SubElement(XMLcommunes, "code_dpt").text = row[0]
        ET.SubElement(XMLcommunes, "code_com").text = row[1]
        ET.SubElement(XMLcommunes, "nom_com").text = row[2]
        ET.SubElement(XMLcommunes, "pop_tot").text = str(row[3])

    #DEPARTEMENTS
    c.execute('SELECT code_dpt, nom_dpt, code_reg FROM Departements')
    for row in c:
        XMLdepartements = ET.SubElement(XMLdatabase, "departements")
        ET.SubElement(XMLdepartements, "code_dpt").text = row[0]
        ET.SubElement(XMLdepartements, "nom_dpt").text = row[1]
        ET.SubElement(XMLdepartements, "code_reg").text = row[2]

    #REGION
    c.execute('SELECT code_reg, nom_reg FROM Region')
    for row in c:
        XMLregion = ET.SubElement(XMLdatabase, "region")
        ET.SubElement(XMLregion, "code_reg").text = row[0]
        ET.SubElement(XMLregion, "nom_reg").text = row[1]

    tree = ET.ElementTree(XMLdatabase)
    tree.write(nom_xml)
    c.close()