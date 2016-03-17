#!/usr/bin/env python
# -*- coding: utf-8 -*-

a=lambda x,y:x%y

for x in range(2,1000):
	prime=1
	
	sum=0
	sum=sum+x
	
	for y in range (2,x):
		if x%y==0:
			prime=0
			#break
			print 0
	if prime :
		print 1
		
print u'質數和為%d' %sum