# Author: Paul Arelt
# 2019 All Rights Reserved

import math
import re

def getRoundedString(numb):
	retStr = str(numb)
	reComp = re.match(r'(\d+)[.]\d*', str(numb))
	
	if reComp:
		retStr = reComp.group(1)

	return retStr


principal = int(input('Enter_Principal\n'))
rate = int(input('Enter_Rate in Percent\n'))
years = int(input('Enter Number of Years to cycle\n'))


rate = rate / 100

if principal <= 0:
	print("Rounding principal to 1 dollar")
	principal = 1

if rate <= 0:
	print("Rounding rate to 1 percent")
	rate = 1

if years <= 0:
	print("Rounding years to 1 year")
	years = 1


total = round(principal, 2)
i = 0

while i < years:
	total += (total * rate)
	yearStr = str(i + 1)
	
	print(yearStr,"years total(rounded):", getRoundedString(total))
		
	i += 1

print("Total", getRoundedString(total))
