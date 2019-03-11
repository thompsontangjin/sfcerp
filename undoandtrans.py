# -*- coding: utf-8 -*-
import function
from  database import database



######trans together
def transbanu(banu,quan,oldwana,newwana):
    df=gettobetransinfo(banu,oldwana)
    nwquan=getnewwanaquan(banu,newwana)
    putinstock(df,newwana,quan,nwquan)
#####get appoined banu in appoined wana created a DataFrame style recording.
def gettobetransinfo(banu,wana):
	sql="select * from stocktable where banu=%s and wana=%s"
	rs=database.query(sql,banu,wana)
	if len(rs)>0:
		df=function.pd.DataFrame(rs)
	else:df=''
	return df
#####get appoined banu in new wana created a DataFrame style recording.
def getnewwanaquan(banu,nwana):
	sql="select * from stocktable where banu=%s and wana=%s"
	rs=database.query(sql,banu,nwana)
	if len(rs)>0:
            df=function.pd.DataFrame(rs)
            nquan=df.quan[0]
	else:
            nquan=-1
	return nquan
#######插入单条库存记录，如果这个批号在这个库存已记录则数量更新##########################################################################################################
def putinstock(df,nwana,nquan,nwquan):###get tobetrans banu info and new wana,new quan,decrease quan in old wana and inser to new wana with new quan.

	ewda=function.strtoday()
        sqlst="insert into stocktable (mana,banu,exda,past,pagw,quan,wana,ewda,pana) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        sqlu="update stocktable set quan=%s,ewda=%s where banu=%s and wana=%s"
        if df.quan[0]>nquan:
            if nwquan>-1:
                    squan=float(nwquan)+float(nquan)
                    database.execute(sqlu,squan,ewda,df.banu[0],nwana)
            else:
                    database.execute(sqlst,df.mana[0],df.banu[0],df.exda[0],df.past[0],df.pagw[0],nquan,nwana,ewda,df.pana[0])
            ###decreas old wana quan
            updateoldwanaquan(df,nquan)
        elif df.quan[0]==nquan:
                    if nwquan>0:
                        squan=float(nwquan)+float(nquan)
                        database.execute(sqlu,squan,ewda,df.banu[0],nwana)
                    else:
                        database.execute(sqlst,df.mana[0],df.banu[0],df.exda[0],df.past[0],df.past[0],nquan,nwana,ewda,df.pana[0])
                ##delete old wana recording
                    deloldwanarecording(df.banu[0],df.wana[0])
        else:
            pass
########update old wana quan
def updateoldwanaquan(df,nquan):
    squan=float(df.quan[0])-float(nquan)
    sql="update stocktable set quan=%s where banu=%s and wana=%s"
    database.execute(sql,squan,df.banu[0],df.wana[0])

########delete old wana recording
def deloldwanarecording(banu,wana):
    sql="delete from stocktable where banu=%s and wana=%s"
    database.execute(sql,banu,wana)
    

    
    
##undo delievery from delieverytable to stocktable due to saon.first step,select data from delieverytable due to saon and show on web to be confirm.then,after confirming,write these data to stocktable and delete these data in delieverytable.##
def undo(saon):
    sql="select * from delieverytable where saon=%s"
    rec=database.query(sql,saon)
    if len(rec)>0:
        df=function.pd.DataFrame(rec)
        return df[['wana','mana','banu','exda','past','quan']]
    else:
        df=""
        return df
        
 #############根据出货文件号删除出货记录
def delsaonfromdelievery(saon):
	function.database.execute("delete from delieverytable where saon=%s",saon)
	function.database.execute("delete from saoncustomertable where saon=%s",saon)
#################################################################################################################	

########将已出货明细还库存表。毛重根据包装规格和批号从进货表中查找。
def undodelievery(saon):
    df=undo(saon)
    n=0
    while n<len(df):
        inorupdatestock(df.ix[n])
        n=n+1
    delsaonfromdelievery(saon)



#######insert or update into stocktable
def inorupdatestock(dfe):
    ewda=function.strtoday()
    sqli="insert into stocktable (wana,mana,banu,exda,past,quan,pagw,ewda,pana) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    sqlu="update stocktable set quan=%s where banu=%s and wana=%s"
    sqlq="select * from stocktable where banu=%s and wana=%s"
    pagw=findpagw(dfe.banu,dfe.past)
    rs=database.query(sqlq,dfe.banu,dfe.wana)
    if len(rs)>0:
        nwquan=getnewwanaquan(dfe.banu,dfe.wana)
        squan=float(nwquan)+float(dfe.quan)
        database.execute(sqlu,squan,dfe.banu,dfe.wana)
    else:
        database.execute(sqli,dfe.wana,dfe.mana,dfe.banu,dfe.exda,dfe.past,dfe.quan,pagw,ewda,"公斤/桶".decode('utf8'))
        
    

########毛重根据包装规格和批号从进货表中查找
def findpagw(banu,past):
    sql="select * from putinwhtable where banu=%s and past=%s"
    rs=database.query(sql,banu,past)
    if len(rs)>0:
        df=function.pd.DataFrame(rs)
        pagw=df.pagw[0]
    else:
        pagw=-1
    return pagw


#############################################################################################		
if __name__ == '__main__':
	#transbanu('AQH06770GN',21,'北京','广州')
    undodelievery('saon')
    
    
