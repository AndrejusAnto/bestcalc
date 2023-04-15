from typing import Union, Optional
from decimal import Decimal

class Calculator:
	'''Simple OOP style calculator that supports add(summation), subtract, multiply, divide,
	take (n) root of current value and reset - to reset a current value to 0. Implemented using
	python's Decimal because of representation of binary fractions like:
	1.1 + 2.2 == 3.3000000000000003, not 3.3.
	'''

	def __init__(self):
		# Initializing default value as 0
		self.result: Union[int, Decimal] = 0

	def __str__(self):
		return f'{self.result}'
		
	def add(self, number: Union[int, float])->Optional[Union[int, Decimal]]:
		try:
			operation = Decimal(str(self.result)) + Decimal(str(number))
			try:
				self.result = int(str(operation))
			except:
				self.result = operation
			return self.result
		except OverflowError as e:
			raise e
	
	def subtract(self, number: Union[int, float])->Union[int, Decimal]:
		operation = Decimal(str(self.result)) - Decimal(str(number))
		try:
			self.result = int(str(operation))
		except:
			self.result = operation
		return self.result
	
	def multiply(self, number: Union[int, float])->Union[int, Decimal]:
		operation = Decimal(str(self.result)) * Decimal(str(number))
		try:
			self.result = int(str(operation))
		except:                
			self.result = operation
		return self.result
		
	def divide(self, number: Union[int, float])->Optional[Union[int, Decimal]]:
		try:
			operation = Decimal(str(self.result)) / Decimal(str(number))
			try:
				self.result = int(str(operation))
			except:            
				self.result = operation
			return self.result
		
		# Catching ZeroDivisionError
		except ZeroDivisionError:
			raise ZeroDivisionError
	
	def n_root(self, number: Union[int, float])->Union[int, Decimal]:
		'''Take number root of a result. Because root of number is automatically a float like 
		3.000000000000000000000000000, so to return int or Decimal, you can save int part to int_value, 
		decimal numbers to decimal_values then sum it and then if sum of decimal_values is > 0, 
		return result as Decimel else as int.
		'''
		operation = Decimal(str(self.result)) ** (Decimal(str(number))**-1)

		int_value = str(operation)[0]
		decimal_values = str(operation)[2:]

		if sum([int(i) for i in decimal_values]) > 0:
			self.result = operation
		else:
			self.result = int(int_value)
		return self.result
	
	def reset(self):
		self.result = 0
		return self.result