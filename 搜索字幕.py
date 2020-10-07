# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 14:25:35 2020

@author: Aierlma
"""

import requests
import os
import re

x = os.getcwd()
files = os.listdir(x)#取得本目录下所有文件，生成一个列表
print(files)
file1 = open(x+"\\temp.txt","w")
count = 0
for i in files:
    if '-C' in i or '-c' in i:
        continue
    if "[" in i:
        i = re.sub('\\[.*?\\]', '', i)
    
    fanhao = os.path.splitext(i)[0]
    print(fanhao)
    c = ''
    a = requests.get(c) 
    print(c)
    b = a.text
    print("包含字幕的磁力連結" in b)
    if "包含字幕的磁力連結" in b:
        count += 1
        file1.write('' + "\n")
        
file1.close()        
print(count)
