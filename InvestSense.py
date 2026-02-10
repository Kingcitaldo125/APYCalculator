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
		if indx == 2 and (strLen-n) >= 2:
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


principal = float(input('Enter Principal\n'))
rate = float(input('Enter Rate in Percent (APY)\n'))
#cont = float(input('Enter Contribution amount in dollars(per year - no more than $19,000)\n'))
cont = float(input('Enter Contribution amount in dollars(per year)\n'))
years = int(input('Enter Number of Years to cycle(no more than 100)\n'))

freq_input = input('Enter Compounding Frequency\n1. Annual\n2. Semi-Annual\n3. Quarterly\n').strip()
freq_map = {'1': 1, '2': 2, '3': 4}
if freq_input not in freq_map:
	print("Invalid selection. Defaulting to Annual.")
	freq_input = '1'
n_periods = freq_map[freq_input]
freq_labels = {'1': 'Annual', '2': 'Semi-Annual', '3': 'Quarterly'}

rate = rate / 100


if cont <= 0:
	print("Setting contribution amount to $1")
	cont = 1

#if cont > 19000:
#	print("Setting contribution amount to $19,000")
#	cont = 19000

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

period_rate = rate / n_periods

pretotal = round(principal, 2)
total = round(principal, 2)
print('')
print("Starting Principal:", getRoundedString(total))
print("Compounding Frequency:", freq_labels[freq_input], "(" + str(n_periods) + "x per year)")
i = 0


while i < years:
	for _ in range(n_periods):
		pretotal += ((pretotal * period_rate)) % totalLimit
		total += (total * period_rate) % totalLimit

	total += cont

	print("Total with no contribution:", getRoundedString(pretotal))
	print("Total with contribution(compounded):", getRoundedString(total))

	yearStr = str(i + 1)

	print(yearStr,"years total(rounded):", getRoundedString(total))
	print('')

	i += 1


print("Contribution-less total:", getRoundedString(pretotal))
print("Total with Contribution(compounded):", getRoundedString(total))
