import sys
sys.path.append('../')

from src.sim import Sim
from src import node
from src import link
from src import packet

from networks.network import Network

import random

class Generator(object):
    def __init__(self,node,destination,load,duration):
        self.node = node
        self.destination = destination
        self.load = load
        self.duration = duration
        self.start = 0
        self.ident = 1

    def handle(self,event):
        # quit if done
        now = Sim.scheduler.current_time()
        if (now - self.start) > self.duration:
            return

        # generate a packet
        self.ident += 1
        p = packet.Packet(destination_address=self.destination,ident=self.ident,protocol='delay',length=1000)
        Sim.scheduler.add(delay=0, event=p, handler=self.node.send_packet)
        # schedule the next time we should generate a packet
        Sim.scheduler.add(delay=random.expovariate(self.load), event='generate', handler=self.handle)