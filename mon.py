from struct import pack
import pandas as pd
import io
import codecs
import os

def xmlToDfRegister(p):
    try:
        l = []
        f = codecs.open(p,'r','UTF-16')
        for i in f:
            row = i.replace('<item>','').replace('</item>','')
            row = row.split('> <')
            rowful = []
            for r in row:
                fild = r.split('>')[1].split('<')[0]
                rowful.append(fild)
            l.append(rowful)
        df = pd.DataFrame(columns=['Account','Fullname','Ispl','Isno','Father','Type','NationalId','Birthday','Serial','Firstname','Lastname'],data=l)

    except:
        df = pd.DataFrame(columns=['Account','Fullname','Ispl','Isno','Father','Type','NationalId','Birthday','Serial','Firstname','Lastname'],data=[])
    return df



dff = pd.DataFrame()
dirlist = 'C:/Users/Moeen/Desktop/Project All/visa (1)/visa/Reg'
dd = os.listdir(dirlist)
for i in dd:
    dirfile =(dirlist+"/"+i)
    df = xmlToDfRegister(dirfile)
    dff = dff.append(df)


dff = dff.drop_duplicates()

dff.to_json('register.json')