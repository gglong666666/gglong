#!/usr/bin/env python
# -*- coding: utf-8 -*-

f=open("zzz3.txt","r")

z=f.readline()
x=len(z)

n=z.count("")
print u"有%d個空白 " %n

m=z.count("e")

print u"有%d個e" %m
print u"共有%d個字" %x

a=n/x
b=m/x

print u"空白占了%f" %round(a,11)
print u"e占了%f" %round(b,11)



















