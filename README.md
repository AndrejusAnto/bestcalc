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
&emsp;pip install -i https://test.pypi.org/simple/ funccalc'''
<br />

Usage:
<br />
&emsp;from funccalc import best_calc as bc
<br />
&emsp;calc = bc.Calculator()
<br />
---
&emsp;calc.add(3)
<br />
&emsp;print(cacl)
<br />
&emsp;3.0
<br />
---
&emsp;calc.sub(5)
<br />
&emsp;print(cacl)
<br />
&emsp;-2.0
<br />
---
&emsp;calc.reset()
<br />
&emsp;print(cacl)
<br />
&emsp;0.0
<br />