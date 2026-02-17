# Author: Paul Arelt
# Use this program at your own risk - the author is not responsible for any accidents that may occur
# 2019 All Rights Reserved

import math
import re

totalLimit = 0xE8D4A51000

# FIXME: rename this function to have a better name
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

# NEW: Ask user for inflation rate
# This allows us to compute real (inflation-adjusted) values.
inflation = float(input('Enter Inflation Rate in Percent\n'))

cont = float(input('Enter Contribution amount in dollars (per year)\n'))
years = int(input('Enter Number of Years to cycle(no more than 100)\n'))

freq_input = input('Enter Compounding Frequency:\n1. Annual\n2. Semi-Annual\n3. Quarterly\n').strip()
freq_map = {'1': 1, '2': 2, '3': 4}
if freq_input not in freq_map:
	print("Invalid Compounding Frequency selection. Defaulting to Annual compounding.")
	freq_input = '1'
n_periods = max(1,freq_map[freq_input])
freq_labels = {'1': 'Annual', '2': 'Semi-Annual', '3': 'Quarterly'}

rate = rate / 100

# NEW: Convert inflation percentage into decimal form
# Example: 3% becomes 0.03
inflation = inflation / 100

# NEW: Prevent negative inflation values
# Negative inflation (deflation) could be supported, but for simplicity and safety we clamp it to 0.
if inflation < 0:
	print("Inflation cannot be negative. Setting inflation to 0%")
	inflation = 0

if cont <= 0:
	print("Setting contribution amount to $1")
	cont = 1

if principal <= 0:
	print("Rounding principal to 1 dollar")
	principal = 1

# FIXED: Previously this incorrectly set rate to 1 (100%).
# We now set it to 1% (0.01 in decimal form).
if rate <= 0:
	print("Rounding rate to 1 percent")
	rate = 0.01

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

# NEW: Display the inflation rate being used
print("Inflation Rate:", inflation * 100, "%")
print('')

i = 0


while i < years:
	for _ in range(n_periods):
		pretotal += ((pretotal * period_rate)) % totalLimit

	total += cont
	for _ in range(n_periods):
		total += (total * period_rate) % totalLimit

	# Number of years elapsed so far
	years_elapsed = i + 1
	# Inflation factor formula:
    # (1 + inflation)^t
    # This represents how much prices have grown over time.
	inflation_factor = (1 + inflation) ** years_elapsed

	# Real value formula:
    # Real Value = Nominal Value / (1 + inflation)^t
    # This converts nominal dollars into purchasing power dollars.
	real_pretotal = pretotal / inflation_factor
	real_total = total / inflation_factor

	print("Nominal total with no contribution:", getRoundedString(pretotal))
	print("Nominal total with contribution (compounded):", getRoundedString(total))

	# NEW: Display inflation-adjusted (real) values
	print("Real total with no contribution (adjusted for inflation):", getRoundedString(real_pretotal))
	print("Real total with contribution (adjusted for inflation):", getRoundedString(real_total))

	yearStr = str(i + 1)

	print(yearStr,"years total (rounded):", getRoundedString(total))
	print('')

	i += 1


# NEW: Compute final inflation factor across all years
final_inflation_factor = (1 + inflation) ** years

# NEW: Final real totals adjusted for total inflation period
print("Final Nominal total with no contribution:", getRoundedString(pretotal))
print("Final Nominal total with contribution (compounded):", getRoundedString(total))

print("Final Real total with no contribution (adjusted for inflation):", getRoundedString(pretotal / final_inflation_factor))
print("Final Real total with contribution (adjusted for inflation):", getRoundedString(total / final_inflation_factor))
