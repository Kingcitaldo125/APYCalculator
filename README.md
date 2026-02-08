# APY Calculator
A calculator for growth of principal over time.
This python script is intended for investors that are seeking to calculate how much their money
will earn over time, regardless of individual contributions.

Individual contributions are being factored in. If you don't want to factor in contributions, no problem.
The script will calculate both pre and post contribution amounts, and show the results on the fly.
For now, this is a simple way to calculate rate of growth over time without contributions coming into play.
This hasn't been fully tested. Proceed with caution. Errors/bugs may be present.

## (F)AQ
Q: How is this unique?
A: None of the other calculators that I have seen, thus far, factor in individual contributions over a period of time. This one will.

Q: What is the compounding frequency?
A: Currently, it's annual. There is, at the time of writing, an issue for adding variable compounding.

Q: Why don't you just use the compounding interest formula directly?
A: For two reasons: 1. Doing this by-hand is fun and 2. It's helpful to see how money grows over time, and by how much. I call this a 'running total'.

## Examples
It will show running totals, which I have not seen from an online calculator, from both pre and post contribution amounts:

For example:
```bash
	P = 65000
	R = 8(percent)
	C = 0
	years = 10
	
	Total after 10 years = $140330
```

Another example:
```bash
	P = 1000
	R = 2
	C = 1
	years = 20
	
	Total after 20 years = $1510
```

## Usage
Run `python InvestSense.py` from a terminal. Your terminal should be ran from the directory where the `InvestSense.py` is present.
This assumes that you have a version of Python 3 already installed and available on your system path.
Follow the prompts to have the script do its thing.
At the end, you will be shown how your money grows over time.
