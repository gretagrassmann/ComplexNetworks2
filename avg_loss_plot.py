import matplotlib.pyplot as plt
import numpy as np
no_edge = "C:\\Users\\Cobal\\Desktop\\ComplexNetworksEXAM\\ComplexNetworks2\\avg_loss_train.txt"
edge = "C:\\Users\\Cobal\\Desktop\\ComplexNetworksEXAM\\ComplexNetworks2\\avg_loss_train_EDGE.txt"

# Import data as a list of numbers
with open(no_edge) as textFile:
    data = textFile.read().split()          # split based on spaces
    data = [float(point) for point in data] # convert strings to floats

with open(edge) as textFile:
    data1 = textFile.read().split()          # split based on spaces
    data1 = [float(point) for point in data1] # convert strings to floats

x = np.arange(1,len(data)+1)

fig = plt.figure()
ax = plt.subplot(111)
ax.plot(x, data, label='Without edges information')
ax.plot(x, data1, label='With edges information')
ax.set_xlabel('Number of epochs')
ax.set_ylabel('Average loss')
plt.title('Comparison ')
ax.legend()
plt.show()
