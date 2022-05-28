#!/usr/bin/python3
import random

###set/get random using size of bc
blank = 0
word = "____"
rang=len(open('../Main/bc').readlines(  ))
num=random.randrange(rang)
fo = open("../Main/bc", "r+")
line = fo.readline()
out=fo.readlines()[num]

##get blank count and print BC
blank += out.count(word)
print out
fo.close()

###set/get random using size of wc
rang=len(open('../Main/wc').readlines(  ))
num=random.randrange(rang)

fo = open("../Main/wc", "r+")
line = fo.readline()
out=fo.readlines()[num]

##print WC
while blank > 0:
    print out
    blank -=1
fo.close()
