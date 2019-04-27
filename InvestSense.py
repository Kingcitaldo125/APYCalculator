# Author: Paul Arelt
# Use this program at your own risk - the author is not responsible for any accidents that may occur
# 2019 All Rights Reserved

import math
import re

totalLimit = 0xE8D4A51000

def commad(strs):
	nStrs = ""
	indx = 0
	revStrs = strs[::-1]
	strLen = len(revStrs)
	for n,i in enumerate(revStrs):
		nStrs += i
		if indx == 2 and (strLen-n) > 2:
			nStrs += ","
			indx = -1
		indx += 1
	
	return nStrs[::-1]

def getRoundedString(numb):
	retStr = str(numb)
	reComp = re.match(r'(\d+)[.]\d*', str(numb))
	
	if reComp:
		retStr = reComp.group(1)

	return "$"+commad(retStr)


principal = int(input('Enter Principal\n'))
rate = float(input('Enter Rate in Percent\n'))
cont = float(input('Enter Contribution amount in dollars(per year - no more than $10,000)\n'))
years = int(input('Enter Number of Years to cycle(no more than 100)\n'))


rate = rate / 100


if cont <= 0:
	print("Setting contribution amount to $1")
	cont = 1
	
if cont > 10000:
	print("Setting contribution amount to $10,000")
	cont = 10000

if principal <= 0:
	print("Rounding principal to 1 dollar")
	principal = 1

if rate <= 0:
	print("Rounding rate to 1 percent")
	rate = 1

if years <= 0:
	print("Rounding years to 1 year")
	years = 1

if years > 100:
	print("Rounding years to 100")
	years = 100


pretotal = round(principal, 2)
total = round(principal, 2)
print('')
print("Starting Principal:", getRoundedString(total))
i = 0


while i < years:
	pretotal += ((pretotal * rate)) % totalLimit
	print("Total with no contribution:", getRoundedString(pretotal))
	
	total += cont
	total += (total * rate) % totalLimit
	print("Total with contribution(compounded):", getRoundedString(total))
	
	yearStr = str(i + 1)
	
	print(yearStr,"years total(rounded):", getRoundedString(total))
	print('')
		
	i += 1


print("Contribution-less total:", getRoundedString(pretotal))
print("Total with Contribution(compounded):", getRoundedString(total))
