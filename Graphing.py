# Run 'pip install matplotlib' on your CLI before running this program
#print('x \t y')

# Basic blank graph
import matplotlib.pyplot as plt
fig, ax = plt.subplots()

# Define dimensions of graph
xmin = int(input('Enter xmin dimension: '))
xmax = int(input('Enter xmax dimension: '))
ymin = int(input('Enter ymin dimension: '))
ymax = int(input('Enter ymax dimension: '))
plt.axis([xmin, xmax ,ymin ,ymax]) # window size
print()

# Display axis lines
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax],'b') # blue y axis


# Plotting
plot_t = int(input('Enter number of plots:  ')) # like how many times are you going to plot points on the graph
print()
for p in range(plot_t):
    p += 1
    print(f'{p} plot')
    x_plot = int(input('Enter x value: '))
    y_plot = int(input('Enter y value: '))
    plt.plot([x_plot],[y_plot], 'ro')
    print()

plt.show()