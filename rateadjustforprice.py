# -*- coding: utf-8 -*-
import speedfair as sf
database=sf.database
####normalfreighttable
nf=database.query("select * from normalfreighttable")
nfdf=sf.pd.DataFrame(nf)
nr=len(nfdf.index)
nc=len(nfdf.columns)-2

###dangerfreighttable
df=database.query("select * from dangerfreighttable")
dfdf=sf.pd.DataFrame(df)
dr=len(dfdf.index)
dc=len(dfdf.columns)-2
def loopupdatepricedanger(df):
    sql1="update dangerfreighttable set "
    sql2=" = %s where id = %s"

    r=0
    c=0
    while r < dr:
        while c < dc:
            nowp=df.iloc[r][c]
            newp=round(round(nowp/1.11,2) *1.1,2)
            sql=sql1+df.columns[c]+sql2
            database.execute(sql,newp,r+1)
            c=c+1
        c=0
        r=r+1
    print "end work dangerfreighttable"


####below for normalfreighttable
def nowprice(df,r,c):
    np=df.iloc[r][c]
    return np
def newprice(nowprice):
    newp=round(round(nowprice/1.11,2) *1.1,2)
    return newp
def updateprice(df,r,c):
    nowp=df.iloc[r][c]
    newp=round(round(nowp/1.11,2) *1.1,2)
    sql1="update normalfreighttable set "
    sql2=" = %s where id = %s"
    sql=sql1+df.columns[c]+sql2
    database.execute(sql,newp,r+1)
    #print df.columns[c]
    #print r
    #print c
def loopupdateprice(df):
    sql1="update normalfreighttable set "
    sql2=" = %s where id = %s"

    r=0
    c=0
    while r < nr:
        while c < nc:
            nowp=df.iloc[r][c]
            newp=round(round(nowp/1.11,2) *1.1,2)
            sql=sql1+df.columns[c]+sql2
            database.execute(sql,newp,r+1)
            c=c+1
        c=0
        r=r+1
    print "end work normalfreighttable"
        
if __name__ == "__main__":
    loopupdateprice(nfdf)
    loopupdatepricedanger(dfdf)
    
    
    
    