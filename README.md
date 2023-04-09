Updated for OOP style calculator.
<br />
Installation (better use virtual env, like conda, mamba or venv):
<br />
pip install -i https://test.pypi.org/simple/ funccalc
<br />
Simple calculator that supports these functions:
<br />
reset() - reset current value to 0.
<br />
add(number) - add a number to a current value, default value is 0.
<br />
sub(number) - subtract a number from a current value.
<br />
multi(number) - multiply a current value by number.
<br />
div(number) - divide a current value by number.
<br />
n_root(number) - take number root of a current value.
<br />
Usage:
<br />
from funccalc import best_calc as bc
<br />
calc = bc.Calculator()
<br />
calc.add(3)
<br />
calc.reset()