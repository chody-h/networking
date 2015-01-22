import optparse
import sys

import matplotlib.pyplot as plt
import matplotlib
from pylab import *

# Class that parses a file and plots several graphs
class Plotter:
    def __init__(self):
        self.x = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.98]
        self.y = [  0.000463, 
                    0.001016, 
                    0.001702, 
                    0.002650, 
                    0.003899, 
                    0.006066, 
                    0.009240, 
                    0.016074, 
                    0.032784, 
                    0.081299, 
                    0.205917]

    def combinedPlot(self):
        """ Create a graph that includes a line plot and a boxplot. """
        clf()
        ax = plt.figure().add_subplot(111)

        # plot the data
        plot(self.x, self.y, label='Theory')

        # plot the equation
        # u = 125                           # service rate = 1/transmission delay = R / L
        p = np.arange(0, 0.995, 0.001)      # utilization
        y = []
        for i in range(0, len(p)):
            y.append(1.0/(2.0*125.0) * (p[i])/(1.0-(p[i])))
        plot(p, y, label='Average')

        # set up the axis
        xlabel('Utilization')
        ax.set_xticks(np.arange(0,1.1,0.1))
        ylabel('Average Queue Duration')
        ax.set_yticks(np.arange(0,0.7,0.1))

        # create a legend
        legend = ax.legend(loc='upper left', shadow=True)

        #print it out
        savefig('outputs/lab1_final.png')

if __name__ == '__main__':
    p = Plotter()
    p.combinedPlot()