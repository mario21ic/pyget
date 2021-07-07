#!/usr/bin/env python

import requests
import subprocess
import sys
import os

import lxml.html as lh
import logging


logging.basicConfig(filename='pyget.log', filemode='w', \
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', \
    level=logging.DEBUG)

def main(url, dir_dest):
    print("## Start ##")
    page = requests.get(url)
    doc = lh.fromstring(page.content)

    a_elements = doc.xpath('//a')
    i=0
    links=[]
    for a in range(5, len(a_elements)):
        A=a_elements[a].get("href")
        links.append(A)
        i+=1

    if not os.path.isdir(dir_dest):
        print("Creating %s" % dir_dest)
        os.mkdir(dir_dest)
    os.chdir(dir_dest)
    for l in links:
        try:
            print("=====")
            file_name = l
            print("file_name:", file_name)
            file_url = url + file_name
            print("file_url:", file_url)
            file_req = requests.get(file_url)
            file_cont = file_req.content
            #print(file_cont)
            open(file_name, 'wb').write(file_cont)
        except Exception as e:
            print("File %s downloading error: %s" % (file_name, str(e)))
            logging.error(str(e))


if __name__=="__main__":
    if len(sys.argv)!=3:
        print("usage:\n./main.py http://mywebsite.com/dir $PWD/tmp")
        exit(1)
    main(sys.argv[1], sys.argv[2])

