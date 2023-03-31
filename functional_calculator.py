from typing import Type

def add(n1: int|float, n2: int|float)->int|float:
	return n1 + n2


def sub(n1: int|float, n2: int|float)-> int|float:
	return n1 - n2

 
def multi(n1: int|float, n2: int|float)-> int|float:
	return n1 * n2


def div(n1: int|float, n2: int|float)-> int|float|Type[Exception]:
	try:
		return n1 / n2
	except ValueError:
		return ValueError


def n_root(n1: int|float, n2: int|float)-> int|float:
	return n1 ** (n2**-1)


def reset()->int:
	return 0


def calc(*args)->int:
	if args:
		return args[0]
	else:
		return 0