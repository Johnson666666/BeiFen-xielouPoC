import requests
import time
with open("url.txt", 'r') as temp:
    for url in temp.readlines():
        url = url.strip('\n')
        with open("web.txt", 'r') as web:
            webs = web.readlines()
        w = open('write.txt', 'w+')
        for web in webs:
            web = web.strip()
            u = url + web
            r = requests.get(u)
            # print("url为:"+u)
            print("url为:" + u + ' ' + "状态为:%d" %r.status_code)
            time.sleep(1)       #想睡多久看自己~
            w.write("url为:" + u + ' ' + "状态为:%d" %r.status_code + '\n')