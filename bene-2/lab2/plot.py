import optparse
import sys

import matplotlib.pyplot as plt
import matplotlib
from pylab import *

# Class that parses a file and plots several graphs
class Plotter:
    def __init__(self):
        # x
        self.window = [1000, 2000, 5000, 10000, 15000, 20000]
        # y1
        self.throughput = [0.201,0.393,0.929,2.836,3.703,4.418]
        # y2
        self.avg_queue = [4.880,2.441,0.974,0.250,0.168,0.124]

    def plot1(self):
        clf()
        ax = plt.figure().add_subplot(111)

        # plot the data
        plot(self.window, self.throughput, label='Throughput')

        # set up the axis
        xlabel('Window Size (bytes)')
        ax.set_xticks(np.arange(0,22000,2000))
        ylabel('Throughput (Mb/sec)')
        ax.set_yticks(np.arange(0,5.5,.5))

        # create a legend
        # legend = ax.legend(loc='upper left', shadow=True)

        #print it out
        savefig('outputs/lab2_throughput.png')

    def plot2(self):
        clf()
        ax = plt.figure().add_subplot(111)

        # plot the data
        plot(self.window, self.avg_queue, label='Average Queue per Packet')

        # set up the axis
        xlabel('Window Size (bytes)')
        ax.set_xticks(np.arange(0,22000,2000))
        ylabel('Average Queue Duration (ms)')
        ax.set_yticks(np.arange(0,5.5,.5))

        # create a legend
        # legend = ax.legend(loc='upper left', shadow=True)

        #print it out
        savefig('outputs/lab2_queue.png')

if __name__ == '__main__':
    p = Plotter()
    p.plot1()
    p.plot2()