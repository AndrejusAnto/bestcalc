from typing import Union, Optional
from decimal import Decimal


def int_or_decimal(operation):
	'''Returns int or Decimal type. Because Decimal have a very long precision 
	and int could be represented like 3.000000000000000000000000000, so to make just 3,
	save int part to int_value, decimal numbers to decimal_numbers then sum it and 
	then if sum of decimal_numbers is != 0, return result as Decimal else as int.
	'''

	# Some number can be like 4.76837158203125e-07 and is Decimal. Representation of 
	# this kind of number in Decimal is with "E", not "e", so first "if" is for
	# skipping a need to return int type.
	if "E" not ins str(operation):
		# This part for checking int or Decimal 
		if "." in str(operation):
			int_value, decimal_numbers = str(operation).split(".")
			if sum([int(i) for i in decimal_numbers]) != 0:
				value = Decimal(str(float(operation)))
			else:
				value = int(int_value)
		else:
			value = int(operation)
	else:
		return operation
	return value


class Calculator:
	'''Simple OOP style calculator that supports add(summation), subtract, multiply, divide,
	take (n) root of current value and reset - to reset a current value to 0. Implemented using
	python's Decimal because of representation of binary fractions:
	1.1 + 2.2 is 3.3000000000000003, not 3.3.
	'''

	def __init__(self):
		# Initializing default value as 0
		self.result: Union[int, Decimal] = 0

	def __str__(self):
		return f'{self.result}'
		
	def add(self, number: Union[int, float])->Optional[Union[int, Decimal]]:
		try:
			operation = Decimal(str(self.result)) + Decimal(str(number))
			self.result = int_or_decimal(operation)
			return self.result
		except OverflowError as e:
			raise e
	
	def subtract(self, number: Union[int, float])->Union[int, Decimal]:
		operation = Decimal(str(self.result)) - Decimal(str(number))
		self.result = int_or_decimal(operation)
		return self.result
	
	def multiply(self, number: Union[int, float])->Union[int, Decimal]:
		operation = Decimal(str(self.result)) * Decimal(str(number))
		self.result = int_or_decimal(operation)
		return self.result
		
	def divide(self, number: Union[int, float])->Optional[Union[int, Decimal]]:
		try:
			operation = Decimal(str(self.result)) / Decimal(str(number))
			self.result = int_or_decimal(operation)
			return self.result
		
		# Catching ZeroDivisionError
		except ZeroDivisionError:
			raise ZeroDivisionError
	
	def n_root(self, number: Union[int, float])->Union[int, Decimal]:
		# Take number root of a result		
		operation = Decimal(str(self.result)) ** (Decimal(str(number))**-1)
		self.result = int_or_decimal(operation)
		return self.result
	
	def reset(self):
		self.result = 0
		return self.result