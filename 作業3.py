#!/usr/bin/env python
# -*- coding: utf-8 -*-

SavedMoney=5000
SM=SavedMoney
print u"請問你要領多少錢 ? ? ?"
print u"請輸入："
Wantmoney=raw_input()
WM=int (Wantmoney)
TotalMoney=SM-WM
TM=TotalMoney

if TM>0:
	print u'你帳戶還有%d元' %TM

elif TM==0:
	print u'你帳戶沒錢囉，快去賺錢吧!!!'

else:
	print u'你帳戶的錢不夠你領噢，要領這麼多錢就先多存點錢進來吧!!!'
	
f=open("ATM.txt","a")
f.write("%d" %TM)
f.close()

