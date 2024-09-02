# Run 'pip install matplotlib' on your CLI before running this program
#print('x \t y')

#for x in range(11):
#    y = 4 * x + 3 # the linear function 
#    print(f'{x} \t {y}')

# Basic blank graph
import matplotlib.pyplot as plt
fig, ax = plt.subplots()

# Define dimensions of graph
xmin = -10
xmax = 10
ymin = -10
ymax = 10
plt.axis([xmin, xmax ,ymin ,ymax]) # window size

# Display axis lines
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax],'b') # blue y axis

# Plotting
plot_t = int(input('Enter number of plots:  ')) # like how many times are you going to plot points on the graph
for p in range(plot_t):
    x_plot = int(input('Enter x value: '))
    y_plot = int(input('Enter y value: '))

    plt.plot([x_plot],[y_plot], 'ro')

plt.show()