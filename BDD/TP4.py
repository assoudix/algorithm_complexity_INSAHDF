#!/usr/bin/python3

import sqlite3 as sql

def connexion_base(adr):
    cn=sql.connect(adr)
    cr=cn.cursor()
    return cn, cr

def creer_table(cr,cn):
    cr.execute("create table if not exists Cercle (IdCercle integer primary key, Rayon real, Ox integer, Oy integer);")
    cn.commit()

def fermer_base(adr):
    adr.close()

'''
def inserer(cr, cn, info):
    cr.execute("select IdCercle from Cercle")
    ID_list=list(cr) #Liste des pk

    for ligne in info:
        if ligne[0] is in ID_list:
            print("Violation de contrainte PK")
            pass
        else:
            cr.execute("insert into Cercle Values"+ligne+";")
    cn.commit()

'''

def inserer(cr, cn, info):
    for ligne in info:
        cr.execute("select * from Cercle where IdCercle=?;", [ligne[0]])
        res=list(cr)

        if len(res)==0:
            cr.execute("insert into Cercle values(?,?,?,?);", ligne)
            cn.commit

def informations_cercle(cr)
    cr.execute("select IDCercle, 2*3.14*rayon, 3.14*rayon*rayon from Cercle;")