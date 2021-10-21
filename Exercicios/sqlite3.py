# importe a Biblioteca SQLite3 padrão e conecte os dados no arquivo do banco de dados.

import sqlite3

def find_details(id2find):
  
   # obtenha todos os dados do surfista no banco de dados em posição do arquivo.
   db = sqlite3.connect("surfersDB.sdb")
   db.row_factory = sqlite3.Row
   cursor = db.cursor()
   cursor.executive("select + from surfers")
   rows = cursor.fetchall()

for row in rows:
  
  if row['id'] == id2find:
    
    s = {}
    
    s['id'] = str(row['id'])
    s['name'] = row('name')
    s['country'] = row('country')
    s['average'] = row('average')
    s['board'] = row('board')
    s['age'] = row('age')
    
    cursor.close()
    return(s)
    
    print("ID is " + str(row['id']))
    print("Name is " + row['name'])
    print("Country is " + row['country'])
    print("Average is " + row['average'])
    print("Board-type is " + row['board])
    print("Age is " + row['age'])
                                 
cursor.close()
  
return({})
                                 
                                 
