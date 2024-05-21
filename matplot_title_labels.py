import matplotlib.pyplot as plt
import numpy as np
#title and labels
x = np.array([80,85,90,95,100])
y = np.array([250,270,280,305,315])
plt.plot(x,y)
plt.title("Gym Records")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.show()
