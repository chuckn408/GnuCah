#!/usr/bin/python3
import random

###set/get random using size of bc
rang=len(open('../Main/bc').readlines(  ))
num=random.randrange(rang)
word = "____"
fo = open("../Main/bc", "r+")
line = fo.readline()
out=fo.readlines()[num]
inserts = 0

##print stuff here
#print ("loaded: ", fo.name)
#print (num)
print out
fo.close()

#for word in out:
    #dothis....
###set/get random using size of wc
rang=len(open('../Main/wc').readlines(  ))
num=random.randrange(rang)

fo = open("../Main/wc", "r+")
line = fo.readline()
out=fo.readlines()[num]

##print stuff here
#print ("loaded: ", fo.name)
#print (num)
print out
fo.close()

