#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
'''针对子域名挖掘机获取到的所有信息进行过滤，先过滤能正常访问的，分离出正常访问域名和扫描出ip的C段'''

import sys
import getopt
import os
import re

def run():
    try:
        opts,args = getopt.getopt(sys.argv[1:],"hf:",["help","file="])
    except:
        print("Usage:python ipurl.py -f <filename>.")
        sys.exit()

    for opt,value in opts:
        if opt in ("-h","--help"):
            print("Usage:python ipurl.py -f <filename>.")
            sys.exit()
        if opt in ("-f","--file"):
            if not re.findall(r'.txt',value):
                print("Usage:python ipurl.py -f <filename>.")
                sys.exit()
            temp = []
            with open(value,"r") as f:
                for i in f.readlines():
                    if "正常访问" in i:
                        with open("url.txt", "a") as h:
                            j = re.findall(r'[a-zA-Z0-9]{1,15}\.[a-zA-Z0-9]{1,10}\.[a-z]{1,10}', i)
                            h.write(j[0] + "\n")
                        k = re.findall(r'\d+\.\d+\.\d+\.', i)
                        if k not in temp:
                            temp.append(k)

    length = len(temp)
    for i in range(length):
        for m in range(1,255):
            with open("target.txt","a") as f2:
                f2.write(temp[i][0] + str(m) + "\n")

if __name__ == "__main__":
    run()
    print("Successfully!!!")