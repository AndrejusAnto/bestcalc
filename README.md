Updated for OOP style calculator.
<br />
Simple calculator that supports these functions:
<br />
&emsp;reset() - reset a current value to 0.
<br />
&emsp;add(number) - add a number to a current value, default value is 0.
<br />
&emsp;sub(number) - subtract a number from a current value.
<br />
&emsp;multi(number) - multiply a current value by number.
<br />
&emsp;div(number) - divide a current value by number.
<br />
&emsp;n_root(number) - take number root of a current value.
<br />

Installation (better use virtual env, like conda, mamba or venv):
<br />
```console
foo@bar:~$ pip install -i https://test.pypi.org/simple/ funccalc
```
&emsp;pip install -i https://test.pypi.org/simple/ funccalc
<br />

Usage:
<br />
```python
from funccalc import best_calc as bc
calc = bc.Calculator()

calc.add(3)
print(cacl)
>>> 3.0

calc.sub(5.5)
print(cacl)
>>> -2.5

calc.reset()
print(cacl)
>>> 0.0
```