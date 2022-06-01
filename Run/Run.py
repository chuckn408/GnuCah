#!/usr/bin/python3
import random

###set/get random using size of bc
blank = 0
word = "____"
rang=len(open('../Main/bc').readlines(  ))
num=random.randrange(rang)
#BC stuff
fo = open("../Main/bc", "r+")
line = fo.readline()
out=fo.readlines()[num]

##get blank count and print BC
blank += out.count(word)
print out
fo.close()

#open WC stuff

while blank > 0:
    fo = open("../Main/wc", "r+")
    line = fo.readline()
    rang=len(open('../Main/wc').readlines(  ))
    num=random.randrange(rang)
    out=fo.readlines()[num]
    print out
    blank -=1
    #line = fo.readline()
    fo.close()
