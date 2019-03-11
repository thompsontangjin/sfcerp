#备份
mysqldump -u "root" -pSFC2017  datasfcusername > sfcdatabase.sql  #总数据库备份
#mysqldump -u "root" -p  datasfcusername namepwd> sfcdatabasenamepwd.sql  #用户名备份
#mysqldump -u "root" -p  datasfcusername customerinfotable> sfcdatabasecustomerinfotable.sql #客户信息备份
#mysqldump -u "root" -p  datasfcusername cumanatable> sfcdatabasecumanatable.sql #物料号表备份
#mysqldump -u "root" -p  datasfcusername dangerfreighttable> sfcdatabasedangerfreighttable.sql #危险品运价表备份
#mysqldump -u "root" -p  datasfcusername normalfreighttable > sfcdatabasenormalfreighttable.sql #普通货运价表备份
#mysqldump -u "root" -p  datasfcusername stocktable > sfcdatabasestocktable.sql #库存表备份
