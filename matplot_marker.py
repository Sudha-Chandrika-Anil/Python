import matplotlib.pyplot as plt
import numpy as np
#marker, size, edgeclr,faceclr, linestyle, linecolor, linewidth
ypoints = np.array([5, 13, 2, 10])
plt.plot(ypoints, marker = 'H', ms = 20, mec = 'm', mfc = 'hotpink', ls = '-.',c = '#4CAF50',lw = '5' )
plt.show()
