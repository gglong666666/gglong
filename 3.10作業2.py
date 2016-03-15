#!/usr/bin/env python
# -*- coding: utf-8 -*-


print u'請輸入一個數字'
a=raw_input()
z=int(a)
num=0
b=1
while b<=z:
	if z%b==0:
		num=num+1
	b=b+1
if num==2:
	print u'你這是質數哦，你自己知道嗎???'
else:
	print u'你這不是質數，再繼續猜吧!!!'