import requests
import json,os,sys
from time import sleep

__author__ = "laganty"

def chk(card,prx):
    url  = "http://checkccv"
    path = "net/thuvien.php"
    data = 'ajax=1&hamxuly=checkwebsite&sock='+prx+'&listcc='+card+'&delim=%7C&email=0&webcheck=CCV01&sleep=0'
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Referer': 'http://checkccv.net/'
    }
    res = requests.post(url+'.'+path, headers=headers, data=data)
    end = res.json()['msg']
    end1 = end.replace('<b style="color:red;">', '\033[91m')
    end2 = end1.replace('</b>', '')
    end3 = end2.replace('<b style="color:green;">', '\033[1;32m')
    end4 = end3.replace('[Check At CheckCCV.Net]', '\33[93m [Check With CheckCCV.net By @laganty Tool] \033[0m')
    return end4

RED, WHITE, GREEN, END, YELLOW = '\033[91m', '\33[97m', '\033[1;32m', '\033[0m', '\33[93m'

ca = input("{}card  {}:{} ".format(RED,END,GREEN))

if ca is not None:
    cc = ca
    pr = input("{}http live proxy {}: {}".format(RED,END,GREEN))
else:
    print('error try again later...')

if pr is not None:
    proxy = pr
    print("{0}wait{2} while{3} checking{4} your {0}c{2}a{3}r{4}d{1}...".format(RED,END,GREEN,YELLOW,WHITE))
    wt = chk(cc,proxy)
    print(wt)
else:
    print('error try again later...')


