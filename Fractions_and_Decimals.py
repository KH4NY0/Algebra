user_num = input('Enter a decimal number to convert: ')

# i am subtracting 1 , because the len function counts each VALUE!!! in a string
# so we'll remove the decimal point by subtracting 1
exponent = int(len(user_num)) - 1

num = float(user_num)

# Using the exponent to get the numerator 
numerator = int(num * 10 ** exponent)

# Using the exponent to get the denominator
denominator = 10 ** exponent

print(f'The fraction is {numerator} / {denominator}')