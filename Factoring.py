# The modulus finds the remainder
x = 39 % 7
print(x)

print()

# Use the modulus in a loop to find factors
y = 12
for test_factor in range(1, y + 1):
    if y % test_factor == 0:
        print(test_factor)