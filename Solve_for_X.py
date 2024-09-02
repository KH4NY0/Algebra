# Run "pip install sympy" on your CLI before running this program
from sympy import * 

x = symbols('x')

user_value = input('Enter value of y: ')
eq = input(f'Enter equation: {user_value}  =  ')
y = int(user_value)

if y >= 0:
    solution1 = f'{eq} - {user_value}' 
    solution2 = solve(solution1,x)
    for s in solution2:
        print(f'x = {s}')

else:
    solution1 = f'{eq} + {user_value}' 
    solution2 = solve(solution1,x)
    for s in solution2:
        print(f'x = {s}')
    

