import sys
sys.path.append('../')
from src.sim import Sim
from src import node
from src import link
from src import packet
from generator import Generator

from networks.network import Network

import argparse
import random

class DelayHandler(object):
    def receive_packet(self,packet):
        print Sim.scheduler.current_time(),packet.ident,packet.created,Sim.scheduler.current_time() - packet.created,packet.transmission_delay,packet.propagation_delay,packet.queueing_delay

def _2n1():
    print "Running simulation: 2 nodes, scenario 1."

    # parameters
    Sim.scheduler.reset()

    # setup network
    net = Network('networks/2n1.txt')

    # setup routes
    n1 = net.get_node('n1')
    n2 = net.get_node('n2')
    n1.add_forwarding_entry(address=n2.get_address('n1'),link=n1.links[0])
    n2.add_forwarding_entry(address=n1.get_address('n2'),link=n2.links[0])

    # setup app
    d = DelayHandler()
    net.nodes['n2'].add_protocol(protocol="delay",handler=d)

    # send one packet
    p = packet.Packet(destination_address=n2.get_address('n1'),ident=1,protocol='delay',length=1000)
    Sim.scheduler.add(delay=0, event=p, handler=n1.send_packet)

    # # take the link down
    # Sim.scheduler.add(delay=1, event=None, handler=n1.get_link('n2').down)

    # # send one packet (it won't go through)
    # p = packet.Packet(destination_address=n2.get_address('n1'),ident=2,protocol='delay',length=1000)
    # Sim.scheduler.add(delay=1.1, event=p, handler=n1.send_packet)

    # # bring the link up
    # Sim.scheduler.add(delay=2, event=None, handler=n1.get_link('n2').up)

    # # send one packet (and now it goes through)
    # p = packet.Packet(destination_address=n2.get_address('n1'),ident=3,protocol='delay',length=1000)
    # Sim.scheduler.add(delay=2.1, event=p, handler=n1.send_packet)

    # run the simulation
    Sim.scheduler.run()

    print ""

def _2n2():
    print "Running simulation: 2 nodes, scenario 2."

    # parameters
    Sim.scheduler.reset()

    # setup network
    net = Network('networks/2n2.txt')

    # setup routes
    n1 = net.get_node('n1')
    n2 = net.get_node('n2')
    n1.add_forwarding_entry(address=n2.get_address('n1'),link=n1.links[0])
    n2.add_forwarding_entry(address=n1.get_address('n2'),link=n2.links[0])

    # setup app
    d = DelayHandler()
    net.nodes['n2'].add_protocol(protocol="delay",handler=d)

    # send one packet
    p = packet.Packet(destination_address=n2.get_address('n1'),ident=1,protocol='delay',length=1000)
    Sim.scheduler.add(delay=0, event=p, handler=n1.send_packet)

    # run the simulation
    Sim.scheduler.run()

    print ""

def _2n3():
    print "Running simulation: 2 nodes, scenario 3."

    # parameters
    Sim.scheduler.reset()

    # setup network
    net = Network('networks/2n3.txt')

    # setup routes
    n1 = net.get_node('n1')
    n2 = net.get_node('n2')
    n1.add_forwarding_entry(address=n2.get_address('n1'),link=n1.links[0])
    n2.add_forwarding_entry(address=n1.get_address('n2'),link=n2.links[0])

    # setup app
    d = DelayHandler()
    net.nodes['n2'].add_protocol(protocol="delay",handler=d)

    # send one packet
    p = packet.Packet(destination_address=n2.get_address('n1'),ident=1,protocol='delay',length=1000)
    Sim.scheduler.add(delay=0, event=p, handler=n1.send_packet)
    p = packet.Packet(destination_address=n2.get_address('n1'),ident=2,protocol='delay',length=1000)
    Sim.scheduler.add(delay=0, event=p, handler=n1.send_packet)
    p = packet.Packet(destination_address=n2.get_address('n1'),ident=3,protocol='delay',length=1000)
    Sim.scheduler.add(delay=0, event=p, handler=n1.send_packet)
    p = packet.Packet(destination_address=n2.get_address('n1'),ident=4,protocol='delay',length=1000)
    Sim.scheduler.add(delay=2, event=p, handler=n1.send_packet)

    # run the simulation
    Sim.scheduler.run()

    print ""

def _3n1a():
    print "Running simulation: 3 nodes, scenario 1a."

    # parameters
    Sim.scheduler.reset()

    # setup network
    net = Network('networks/3n1a.txt')

    # setup routes
    n1 = net.get_node('n1')
    n2 = net.get_node('n2')
    n3 = net.get_node('n3')
    n1.add_forwarding_entry(address=n2.get_address('n1'),link=n1.links[0])
    n1.add_forwarding_entry(address=n3.get_address('n2'),link=n1.links[0])

    n2.add_forwarding_entry(address=n1.get_address('n2'),link=n2.links[0])
    n2.add_forwarding_entry(address=n3.get_address('n2'),link=n2.links[1])

    n3.add_forwarding_entry(address=n2.get_address('n3'),link=n3.links[0])
    n3.add_forwarding_entry(address=n1.get_address('n2'),link=n3.links[0])

    # setup app
    d = DelayHandler()
    net.nodes['n1'].add_protocol(protocol="delay",handler=d)
    net.nodes['n2'].add_protocol(protocol="delay",handler=d)
    net.nodes['n3'].add_protocol(protocol="delay",handler=d)

    # send a 1 MB file, split into 1kB packets, from n1 to n3
    for i in range(1, 1001):
        p = packet.Packet(destination_address=n3.get_address('n2'),ident=1,protocol='delay',length=1000)
        Sim.scheduler.add(delay=0, event=p, handler=n1.send_packet)

    # run the simulation
    Sim.scheduler.run()

    print ""

def _3n1b():
    print "Running simulation: 3 nodes, scenario 1b."

    # parameters
    Sim.scheduler.reset()

    # setup network
    net = Network('networks/3n1b.txt')

    # setup routes
    n1 = net.get_node('n1')
    n2 = net.get_node('n2')
    n3 = net.get_node('n3')
    n1.add_forwarding_entry(address=n2.get_address('n1'),link=n1.links[0])
    n1.add_forwarding_entry(address=n3.get_address('n2'),link=n1.links[0])

    n2.add_forwarding_entry(address=n1.get_address('n2'),link=n2.links[0])
    n2.add_forwarding_entry(address=n3.get_address('n2'),link=n2.links[1])

    n3.add_forwarding_entry(address=n2.get_address('n3'),link=n3.links[0])
    n3.add_forwarding_entry(address=n1.get_address('n2'),link=n3.links[0])

    # setup app
    d = DelayHandler()
    net.nodes['n2'].add_protocol(protocol="delay",handler=d)
    net.nodes['n3'].add_protocol(protocol="delay",handler=d)

    # send a 1 MB file, split into 1kB packets, from n1 to n3
    for i in range(1, 1001):
        p = packet.Packet(destination_address=n3.get_address('n2'),ident=1,protocol='delay',length=1000)
        Sim.scheduler.add(delay=0, event=p, handler=n1.send_packet)

    # run the simulation
    Sim.scheduler.run()

    print ""

def _3n2():
    print "Running simulation: 3 nodes, scenario 2."

    # parameters
    Sim.scheduler.reset()

    # setup network
    net = Network('networks/3n2.txt')

    # setup routes
    n1 = net.get_node('n1')
    n2 = net.get_node('n2')
    n3 = net.get_node('n3')
    n1.add_forwarding_entry(address=n2.get_address('n1'),link=n1.links[0])
    n1.add_forwarding_entry(address=n3.get_address('n2'),link=n1.links[0])

    n2.add_forwarding_entry(address=n1.get_address('n2'),link=n2.links[0])
    n2.add_forwarding_entry(address=n3.get_address('n2'),link=n2.links[1])

    n3.add_forwarding_entry(address=n2.get_address('n3'),link=n3.links[0])
    n3.add_forwarding_entry(address=n1.get_address('n2'),link=n3.links[0])

    # setup app
    d = DelayHandler()
    net.nodes['n2'].add_protocol(protocol="delay",handler=d)
    net.nodes['n3'].add_protocol(protocol="delay",handler=d)

    # send a 1 MB file, split into 1kB packets, from n1 to n3
    for i in range(1, 1001):
        p = packet.Packet(destination_address=n3.get_address('n2'),ident=1,protocol='delay',length=1000)
        Sim.scheduler.add(delay=0, event=p, handler=n1.send_packet)

    # run the simulation
    Sim.scheduler.run()

    print ""

def _qt():
    print "Running simulation: queueing theory."

    # parameters
    Sim.scheduler.reset()

    # setup network
    net = Network('../networks/one-hop.txt')

    # setup routes
    n1 = net.get_node('n1')
    n2 = net.get_node('n2')
    n1.add_forwarding_entry(address=n2.get_address('n1'),link=n1.links[0])
    n2.add_forwarding_entry(address=n1.get_address('n2'),link=n2.links[0])

    # setup app
    d = DelayHandler()
    net.nodes['n2'].add_protocol(protocol="delay",handler=d)

    # setup packet generator
    destination = n2.get_address('n1')
    max_rate = 1000000/(1000*8)
    load = 0.8*max_rate
    g = Generator(node=n1,destination=destination,load=load,duration=10)
    Sim.scheduler.add(delay=0, event='generate', handler=g.handle)
    
    # run the simulation
    Sim.scheduler.run()

    print ""

if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog='Network Simulation', description='Project 1 of CS 460 at BYU.', add_help=True)
    # valid arguments for -s:
    # all 2n1 2n2 2n3 3n1a 3n1b 3n2 qt
    parser.add_argument('-s', '--sim', type=str, action='store', default='all', help='Specify which simulation you want to run. Valid arguments are [all | 2n1 | 2n2 | 2n3 | 3n1 | 3n2 | qt].')
    args = parser.parse_args()
    sims = args.sim

    if sims == "all":
        _2n1()
        _2n2()
        _2n3()
        _3n1a()
        _3n1b()
        _3n2()
        _qt()
    elif sims == "2n1":
        _2n1()
    elif sims == "2n2":
        _2n2()
    elif sims == "2n3":
        _2n3()
    elif sims == "3n1a":
        _3n1a()
    elif sims == "3n1b":
        _3n1b()
    elif sims == "3n2":
        _3n2()
    elif sims == "qt":
        _qt()
    else:
        print "Simulation not implemented. Use the help command [python sim.py --help] for more."