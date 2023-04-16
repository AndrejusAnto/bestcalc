from hypothesis import given, assume, strategies as st
from decimal import Decimal
import best_calc as bc
import pytest


def test_reset():
	# Testing the output of `reset` function aka reset to 0
	calc = bc.Calculator()
	calc.add(9)
	assert calc.reset() == 0


@given(n=st.integers(min_value=-1_000_000_000, max_value=1_000_000_000))
def test_add_hypo_int(n):
	# Testing `add` function with hypothesis for int type
	calc = bc.Calculator()
	for _ in range(2):
		init_value = calc.result
		assert calc.add(n) == init_value + n


@given(n=st.floats(allow_nan=False, allow_infinity=False))
def test_add_hypo_float(n):
	# Testing `add` function with hypothesis for float type
	calc = bc.Calculator()
	assert calc.add(n) == Decimal(str(n))

	
def test_add():
	calc = bc.Calculator()
	assert calc.add(2) == 2
	
	calc.reset()
	for _ in range(5):
		calc.add(0.1)
	assert calc.add(0.1) == Decimal("0.6")


def test_subtract():
	calc = bc.Calculator()
	assert calc.subtract(2) == -2
	assert calc.subtract(2.5) == Decimal("-4.5")

	 
def test_multiply():
	calc = bc.Calculator()

	calc.add(2)
	assert calc.multiply(4) == 8
	assert calc.multiply(2.0) == Decimal("16.0")


def test_divide():
	calc = bc.Calculator()
	calc.add(9)
	assert calc.divide(3) == 3
	assert calc.divide(2) == Decimal("1.5")


	# Testing divided by 0 error
	with pytest.raises(ZeroDivisionError):
		calc.divide(0)

	 
def test_n_root():
	calc = bc.Calculator()
	calc.add(9)
	assert calc.n_root(2) == 3
	calc.add(3.25)
	assert calc.n_root(2) == Decimal("2.5")
