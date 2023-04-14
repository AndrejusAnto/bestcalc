from typing import Union, Optional
from math import fsum

class Calculator:
	'''Simple OOP style calculator that supports add, subtract, multiply, divide,
	take (n) of current value and reset - to reset a current value to 0.
	'''

	def __init__(self):
		'''Initializing default value as 0'''
		self.result: Union[int, float] = 0

	def __str__(self):
		return f'{self.result}'
		
	def add(self, number: Union[int, float])->Optional[Union[int, float]]:
		''' Add a number to result, default == 0. For summation using fsum, because
		1.1 + 2.2 is not exactly 3.3.
		'''	
		try:
			self.result = fsum((self.result, number))
			return self.result
		except OverflowError as e:
			raise e
	
	def subtract(self, number: Union[int, float])->Union[int, float]:
		self.result = self.result - number
		return self.result
	
	def multiply(self, number: Union[int, float])->Union[int, float]:
		self.result = self.result * number
		return self.result
		
	def divide(self, number: Union[int, float])->Optional[Union[int, float]]:
		try:
			self.result = self.result / number
			return self.result
		except ZeroDivisionError:
			raise ZeroDivisionError
	
	def n_root(self, number: int)->Union[int, float]:
		'''Take number root of a result'''
		self.result = self.result ** (number**-1)
		return self.result
	
	def reset(self):
		self.result = 0
		return self.result