import getpass
#import commands
import subprocess
import pymysql
import csv
import time

user=input('Enter user name:')
passwd = getpass.getpass('Enter password:')
command='du -sch /var/lib/mysql/ | grep total'

ser=['10.1.1.1','10.1.1.2','10.1.1.3','10.1.1.4']

for i in range(len(ser)):
	val="sshpass -p ",passwd," ssh -o StrictHostKeyChecking=no ",user,"@",ser[i]," \"",command,"\""
	val="".join(val)
	#print (val)
	rc = subprocess.getstatusoutput(val)
	val=rc[1].split(" ")
	print (val,'-->',ser[i])
    
    