"""
Returns a string as a result of converting the decimal number to the base

int n: The decimal number that is to be converted
int base: The base that is to be converted to
returns String: The converted number
"""
def convert_to_base(n, base):
	s = ''
	while n != 0:
		temp = int(n % base)
		if temp > 9:
			s += chr(temp + 55)
		else:
			s += str(temp)
		n //= base
	return s

""" 
Converts a string from an arbitrary base to decimal

String n:
int base:
returns int: Decimal representation of the number
"""
def convert_from_base(n, base):
	lower_n = n.upper()
	num = 0
	for c in lower_n:
		num *= base
		n_temp = ord(c)
		if n_temp > 57:
			n_temp -= 7
		n_temp -= 48
		num += n_temp
	return num
