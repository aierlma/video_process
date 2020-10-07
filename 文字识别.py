# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 15:35:40 2020

@author: Aierlma
"""

from aip import AipOcr

import re
import os
import time

""" 你的 APPID AK SK """
APP_ID = ''
API_KEY = ''
SECRET_KEY = ''

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

path = os.getcwd()
listimg = [os.path.join(path, f) for f in os.listdir(path) if f.endswith(".jpeg")]

for foo in range(0,260):
    a = 2*foo
    for _ in range(a,a+2):
        file = listimg[_]
        i = open(file, 'rb').read()
        #result = client.basicGeneral(i)#通用
        result = client.basicAccurate(i)#精准
        print(result)

        with open("result.txt", "a", encoding='utf-8') as resfile:
            while "words_result" not in result:
                result = client.basicAccurate(i)
            for item in result['words_result']:
                resfile.write(item['words'])
                resfile.write('\n')
                print(file)
    time.sleep(1)
