# pytest -s tests && mypy functional_calculator.py && pyflakes functional_calculator.py

import functional_calculator as fc
'''This will place the names of all objects from <module_name> into the local symbol table, 
with the exception of any that begin with the underscore (_) character.'''

import pytest

print()
# gal initilize
calculator = fc.calc()
print(calculator)

calculator = fc.calc(4)
print(calculator)

calculator = fc.add(calculator, 6)
print(calculator)
calculator = fc.sub(calculator, 5)
print(calculator)
calculator = fc.reset()
print(calculator)
calculator = fc.add(calculator, 3)
print(calculator)
calculator = fc.multi(calculator, 6)
print(calculator)
calculator = fc.div(calculator, 2)
print(calculator)
calculator = fc.n_root(calculator, 2)
print(calculator)
calculator = fc.n_root(8, 3)
print(calculator)


def test_add():
	"Verify the output of `add` function"
	assert fc.add(2,4) == 6.0

 
def test_sub():
	"Verify the output of `sub` function"
	assert fc.sub(2, 4) == -2.0

	 
def test_multi():
	"Verify the output of `multi` function"
	assert fc.multi(2,4) == 8.0


def test_div():
	"Verify the output of `div` function"
	assert fc.div(2, 4) == .5


def test_zero_div():
	"Verify the output of `div` function divided by 0"
	with pytest.raises(ZeroDivisionError):
		fc.div(1, 0)

	 
def test_n_root():
	"Verify the output of `n_root` function"
	assert fc.n_root(8, 3) == 2
	assert fc.n_root(8.0, 3) == 2.0


def test_reset():
	"Verify the output of `reset` function aka reset to 0"
	assert fc.reset() == 0


def test_calc():
	"Verify the output of `calc` as initialization function with provided number"
	assert fc.calc(6) == 6


def test_init_calc():
	"Verify the output of `calc` as initialization function with zero"
	assert fc.calc() == 0
