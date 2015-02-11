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
        self.throughput = [200675,393078,928817,2835571,3702861,4418301]
        # y2
        self.avg_queue = [4.880,2.441,0.974,0.250,0.168,0.124]

    def plot1(self):
        clf()
        ax = plt.figure().add_subplot(111)

        # plot the data
        plot(self.window, self.throughput, label='Throughput')

        # set up the axis
        xlabel('Window Size in Bytes')
        ax.set_xticks(np.arange(0,20000,2000))
        ylabel('Average Queue Duration')
        ax.set_yticks(np.arange(0,5000000,500000))

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
        xlabel('Average Queue Duration per Packet in ms')
        ax.set_xticks(np.arange(0,20000,2000))
        ylabel('Average Queue Duration')
        ax.set_yticks(np.arange(0,5,.5))

        # create a legend
        # legend = ax.legend(loc='upper left', shadow=True)

        #print it out
        savefig('outputs/lab2_queue.png')

if __name__ == '__main__':
    p = Plotter()
    p.plot1()
    p.plot2()