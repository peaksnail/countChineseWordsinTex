#!/usr/bin/python 
# coding=utf-8 

#func : count the chinese word in tex
#input: the filepath
#output : the number of the chinese words

import sys

if len(sys.argv) == 1 :
    print "usage: python count.py file_namepath"
    sys.exit(1)

file_name = sys.argv[1]
with open(file_name,"r") as f :
    zh=0
    flength=len(f.read())
    f.seek(0)
    while(f.tell() < flength):
        if(ord(f.read(1)) > 127): 
            # calculate the ascii ,if > 127 say it's not popular ascii"
            f.seek(f.tell()+2)
            zh=zh+1
print "汉字加上符号一共有："+str(zh)+" 个字",
