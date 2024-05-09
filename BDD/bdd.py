#!/usr/bin/python3

import sqlite3 as sql
cn=sql.connect("bases_sqlite.db")
cr1=cn.cursor()
cr2=cn.cursor()
#cr1.execute("insert into etudiant (Numet, Nom, Prenom) Values (1997, 'Assoudi', 'Omar'), (1998, 'Assoudi', 'Oussama'), (1, 'Steve', 'Wozniak'), (99, 'Super', 'Mario');")

#################################
ne = 0
while(ne != -1):
    ne=int(input("num d etudiant?"))
    cr2.execute("select * from etudiant where Numet=?;", [ne])
    R=list(cr2)
    print(R)
cr1.close()
cr2.close()
cn.close()