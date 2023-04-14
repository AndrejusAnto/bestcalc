import best_calc as bc
import pytest
from hypothesis import given, assume, strategies as st


def test_reset():
	# Testing the output of `reset` function aka reset to 0
	calc = bc.Calculator()
	calc.add(9)
	assert calc.reset() == 0


@given(n=st.integers(min_value=-1_000_000_000, max_value=1_000_000_000))
def test_add_hypo_int(n):
	# Testing `add` function with hypothesis for int
	calc = bc.Calculator()
	for _ in range(2):
		init_value = calc.result
		assert calc.add(n) == bc.fsum((init_value, n))


@given(n=st.floats(allow_nan=False, allow_infinity=False))
def test_add_hypo_float(n):
	# Testing the output of `add` function with hypothesis for float
	try:
		calc = bc.Calculator()
		init_value = calc.result
		assert calc.add(n) == bc.fsum((init_value, n))
	
	except Exception as exc:
		# Testing `add` function with hypothesis for OverflowError error:
		# when sum of numbers goes to infinity e.g. [8.988465674311579e+307, 8.98846567431158e+307]

		with pytest.raises(exc):
			calc = bc.Calculator()
			for _ in range(2):
				calc.add(n)


def test_add():
	# Testing `add` function
	calc = bc.Calculator()

	assert calc.add(2) == 2
	assert calc.add(4) == 6.0


def test_subtract():
	# Testing `subtract` function
	calc = bc.Calculator()
	assert calc.subtract(2) == -2.0

	calc.add(5)
	assert calc.subtract(2) == 1.0

	 
def test_multiply():
	# Testing `multiply` function
	calc = bc.Calculator()
	calc.add(2)
	assert calc.multiply(4) == 8.0


def test_divide():
	# Testing `divide` function
	calc = bc.Calculator()
	calc.add(9)
	assert calc.divide(3) == 3

	# Testing divided by 0 error
	with pytest.raises(ZeroDivisionError):
		calc.divide(0)

	 
def test_n_root():
	# Testing `n_root` function
	calc = bc.Calculator()
	calc.add(9)
	assert calc.n_root(2) == 3
	calc.add(1.0)
	assert calc.n_root(2.0) == 2.0
