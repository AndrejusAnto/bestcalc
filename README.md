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
```
or
```python
from funccalc.best_calc import Calculator
calc = Calculator()
```
then
```python

calc.add(3)
>>> 3
calc.add(3.1)
>>> Decimal('6.1')
print(calc)
6.1

calc.reset()
print(calc)
>>> 0.0

calc.subtract(5)
>>> -5
calc.subtract(-2.5)
>>> Decimal('-2.5')
print(calc)
>>> -2.5
```