# -*- coding: utf-8 -*-

from database import database

#登陆检查
#装饰器在被装饰函数执行前进入NEWFUNC函数运行。NEWFUNC函数先取出COOKIE值并在数据库里比较验证合法性，如跟数据库存数据一致则执行被装饰函数。否则链接重定向到登陆##页面。

def authenticated(f):
    def newfunc(self):
           username=self.get_secure_cookie('speedfairuser')
           if  username:
               f(self)
           else:self.redirect("/signin")
           return  f
    return newfunc
def checkadmin(f):
	def newfunc(self):
		un=self.get_secure_cookie('speedfairuser')
		if un=='tangjin':
			f(self)
		else:
			self.render("static/msg.html",msg="超出操作权限")
		return f
	return newfunc
def checkdelievery(f):
	def newfunc(self):
		username=self.get_secure_cookie('speedfairuser')
		rec=database.query("select level from namepwd where username=%s",username)
		level=rec[0]['level']
		
		if level =="B":
			f(self)
		else:self.render("static/msg.html",msg="超出操作权限")
		return f
	return newfunc
def checkputinwh(f):
	def newfunc(self):
		username=self.get_secure_cookie('speedfairuser')
		rec=database.query("select level from namepwd where username=%s",username)
		level=rec[0]['level']
		
		if level =="L":
			f(self)
		else:self.render("static/msg.html",msg="超出操作权限")
		return f
	return newfunc
