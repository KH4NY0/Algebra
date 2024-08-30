# Remember to run "pip install sympy" on your CLI before running this program
import sympy
from sympy import symbols
from sympy.solvers import solve

x = symbols('x')

eq = input('Enter equation: 0 =  ')

solution = solve(eq,x)
for s in solution:
    print(f'x = {s}')