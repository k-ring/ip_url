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
<<<<<<< HEAD
            temp = []
=======
>>>>>>> f3e7c587ad93309929d88ca37452a685f3fd5446
            with open(value,"r") as f:
                for i in f.readlines():
                    if "正常访问" in i:
                        with open("url.txt", "a") as h:
                            j = re.findall(r'[a-zA-Z0-9]{1,15}\.[a-zA-Z0-9]{1,10}\.[a-z]{1,10}', i)
                            h.write(j[0] + "\n")
<<<<<<< HEAD
                        k = re.findall(r'\d+\.\d+\.\d+\.', i)
                        if k not in temp:
                            temp.append(k)

    length = len(temp)
    for i in range(length):
        for m in range(1,255):
            with open("target.txt","a") as f2:
                f2.write(temp[i][0] + str(m) + "\n")
=======
                        with open("temp.txt", "a") as p:
                            k = re.findall(r'\d+\.\d+\.\d+\.\d+', i)
                            p.write(k[0] + "\n")

    #去重复的ip
    ip = []
    with open("temp.txt","r") as f1:
        for k in f1.readlines():
            ip.append(k.strip())
        length = len(ip)
        for i in range(length - 1):
            for j in range(i + 1, length):
                if(ip[i] == ip[j]):
                    break
                else:
                    continue
            if(j == length - 1):
                ip1 = re.findall(r"\d+\.\d+\.\d+\.",ip[i])   #扫描了C段
                for m in range(1,255):
                    with open("ip.txt","a") as f2:
                        f2.write(ip1[0]+str(m)+"\n")

    #删除temp.txt文件
    os.remove("temp.txt")
>>>>>>> f3e7c587ad93309929d88ca37452a685f3fd5446

if __name__ == "__main__":
    run()
    print("Successfully!!!")