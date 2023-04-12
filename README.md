Updated for OOP style calculator.
<br />
Simple calculator that supports these methods:
* &emsp;reset() - reset a current value to 0.
* &emsp;add(number) - add a number to a current value, default value is 0.
* &emsp;subtract(number) - subtract a number from a current value.
* &emsp;multiply(number) - multiply a current value by number.
* &emsp;divide(number) - divide a current value by number.
* &emsp;n_root(number) - take number root of a current value.

Installation (better use virtual env, like conda, mamba or venv):
<br />
```console
(fooenv)@bar:~$ pip install -i https://test.pypi.org/simple/ funccalc
```
Usage:
<br />
```python
from funccalc import best_calc as bc
calc = bc.Calculator()

calc.add(3)
print(calc)
>>> 3.0

calc.subtract(5.5)
print(calc)
>>> -2.5

calc.reset()
print(calc)
>>> 0.0
```