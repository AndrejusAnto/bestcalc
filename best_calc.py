from typing import Type, Union, Optional
from math import fsum

class Calculator:
	def __init__(self):
		self.result = 0

	def cur_value(self):
		print(self.result)
		return self.result
		
	def add(self, number: Union[int, float])->Optional[Union[int, float]]:
		''' Add a number to result, default == 0. For summation using fsum, because
		1.1 + 2.2 is not exactly 3.3.
		'''	
		try:
			self.result = fsum((self.result, number))
			print(self.result)
			return self.result
		except OverflowError as e:
			raise e
	
	def sub(self, number: Union[int, float])->Union[int, float]:
		''' Subtract a number from result'''
		self.result = self.result - number
		print(self.result)
		return self.result
	
	def multi(self, number: Union[int, float])->Union[int, float]:
		''' Multiply result by a number'''
		self.result = self.result * number
		print(self.result)
		return self.result
		
	def div(self, number: Union[int, float])->Optional[Union[int, float]]:
		''' Divide result by a number'''
		try:
			self.result = self.result / number
			print(self.result)
			return self.result
		except ZeroDivisionError:
			raise ZeroDivisionError
	
	def n_root(self, number: int)->Union[int, float]:
		''' Take number root of a result'''
		self.result = self.result ** (number**-1)
		print(self.result)
		return self.result
	
	def reset(self):
		''' Reset result to 0'''
		self.result: Union[int, float] = 0
		print(self.result)
		return self.result