import matplotlib.pyplot as plt

y2 = int(input('Enter y2 value: '))
y1 = int(input('Enter y1 value: '))
x2 = int(input('Enter x2 value: '))
x1 = int(input('Enter x1 value: '))

M = (y2 - y1) / (x2 - x1)
print(f'Gradient is {M}')
float(x2)
b = y2 - (M * x2)

if b > 0:
    print(f'Therefore the equation is f(x) = {M}x + {b}')
else:
    print(f'Therefore the equation is f(x) = {M}x {b}')

# Define dimensions of graph
xmin = -10
xmax = 10
ymin = -10
ymax = 10

# For the line on the graph
y3 = M*xmin + b
y4 = M*xmax + b

fig, ax = plt.subplots()
plt.axis([xmin, xmax ,ymin ,ymax]) # window size
# Display axis lines
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax],'b') # blue y axis

# Plot the linear function as a red line
plt.plot([xmin, xmax],[y3,y4], 'r')

plt.show()