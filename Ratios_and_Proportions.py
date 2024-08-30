# n1/d1 = n2/d2 , Ratio and Proportion equation
# n = numerator and d = denominator

print("Enter '0' in unknown variable, it will act as 'x' :) ")
n1 = int(input('Enter value for n1: '))
d1 = int(input('Enter value for d1: '))
n2 = int(input('Enter value for n2: '))
d2 = int(input('Enter value for d2: '))

if n1 == 0:
    answer = d1 * n2 / d2 
    print(f'n1 is {answer}')

if d1 == 0:
    answer = n1 * d2 / n2 
    print(f'd1 is {answer}')

if n2 == 0:
    answer = d2 * n1 / d1
    print(f'n2 is {answer}')

if d2 == 0:
    answer = n2 * d1 / n1
    print(f'd2 is {answer}')
