Updated for OOP style calculator.
<br />
Simple calculator that supports these methods:
<br />
* &emsp;reset() - reset a current value to 0.
<!-- <br /> -->
* &emsp;add(number) - add a number to a current value, default value is 0.
<!-- <br /> -->
* &emsp;subtractnumber) - subtract a number from a current value.
<!-- <br /> -->
* &emsp;multiply(number) - multiply a current value by number.
<!-- <br /> -->
* &emsp;divide(number) - divide a current value by number.
<!-- <br /> -->
* &emsp;n_root(number) - take number root of a current value.
<br />

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
print(cacl)
>>> 3.0

calc.subtract5.5)
print(cacl)
>>> -2.5

calc.reset()
print(calc)
>>> 0.0
```