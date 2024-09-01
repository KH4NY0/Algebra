# Remember to run "pip install sympy" on your CLI before running this program
from sympy import * 


x = symbols('x')

# we are always assuming that y = 0 , but i'll figure out later on how to declare the value of 'y' in the equation
eq = input('Enter equation: y =  ')

solution = solve(eq,x)
print(solution)

solution = solve(eq,x)
for s in solution:
    print(f'x = {s}')