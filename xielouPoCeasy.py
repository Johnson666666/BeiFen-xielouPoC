import requests
import time

url = 'http://44.210.126.137:82'     #这里url末尾不能有'/'
with open("web.txt", 'r') as web:
    webs = web.readlines()
w = open('write easy.txt', 'w+')
for web in webs:
    web = web.strip()
    u = url + web
    r = requests.get(u)
    
    #print("url为:"+u)
    print("url为:" + u + ' ' + "状态为:%d"%r.status_code)
    time.sleep(1)       #想睡多久看自己~
    w.write("url为:" + u + ' ' + "状态为:%d"%r.status_code + '\n')