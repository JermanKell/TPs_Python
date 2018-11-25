import makedatabase
import exportdatabase
import importdatabase


nom_db = "database.db"
#Exercice1
makedatabase.create_database(nom_db)
makedatabase.fill_database(nom_db)

#Exercice2
makedatabase.sum_total_pop_department()
makedatabase.sum_total_pop_region()

#Exercice3
makedatabase.list_department_com()

#Exercice4
nom_xml = "database.xml"
exportdatabase.expdatabase(nom_xml)
importdatabase.impdatabase(nom_xml, 'database2.db')

#Exercice5
makedatabase.modify_database('database2.db')
makedatabase.new_sum_pop()

