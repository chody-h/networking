import time
import sys
sys.path.append('..')

from src.sim import Sim
from src.connection import Connection
from src.tcppacket import TCPPacket
from src.buffer import SendBuffer,ReceiveBuffer

class TCP(Connection):
    ''' A TCP connection between two hosts.'''
    def __init__(self,transport,source_address,source_port,
                 destination_address,destination_port,app=None,window=1000):
        Connection.__init__(self,transport,source_address,source_port,
                            destination_address,destination_port,app)

        ### Sender functionality

        # send buffer
        self.send_buffer = SendBuffer()
        # maximum segment size, in bytes
        self.mss = 1000
        # send window; represents the total number of bytes that may
        # be outstanding at one time. is now dynamic (TCP Tahoe)
        self.window = 1 * self.mss
        # largest sequence number that has been ACKed so far; represents
        # the next sequence number the client expects to receive
        self.sequence = 0
        # retransmission timer
        self.timer = 0
        # timeout duration in seconds
        self.timeout = 1
        # dynamic round trip timer
        self.rtt = 1
        # minimum rtt
        self.min_rtt = 0.2
        # alpha for calculating retranmission timer
        self.alpha = 0.125
        # times certain packets were sent
        self.packet_times = {}
        # standard deviation of round trip time
        self.dev_rtt = 0
        # beta for calculating std deviation
        self.beta = 0.25
        # threshold for TCP Tahoe congestion window
        self.threshold = 100000
        # keep track of duplicate ACKs
        self.duplicates = 0

        ### Receiver functionality

        # receive buffer
        self.receive_buffer = ReceiveBuffer()
        # ack number to send; represents the largest in-order sequence
        # number not yet received
        self.ack = 0

    def trace(self,message):
        ''' Print debugging messages. '''
        Sim.trace("TCP",message)

    def receive_packet(self,packet):
        ''' Receive a packet from the network layer. '''
        if packet.ack_number > 0:
            # handle ACK
            self.handle_ack(packet)
        if packet.length > 0:
            # handle data
            self.handle_data(packet)

    ''' Sender '''

    def send(self,data):
        ''' Send data on the connection. Called by the application. '''
        self.send_buffer.put(data)
        while self.send_buffer.available() > 0 and self.send_buffer.outstanding() < self.window:
            if self.send_buffer.outstanding() + self.mss > self.window:
                (seg_data,i) = self.send_buffer.get(self.window - self.send_buffer.outstanding())
            else:
                (seg_data,i) = self.send_buffer.get(self.mss)
            self.send_packet(seg_data,i)

    def send_packet(self,data,sequence):
        packet = TCPPacket(source_address=self.source_address,
                           source_port=self.source_port,
                           destination_address=self.destination_address,
                           destination_port=self.destination_port,
                           body=data,
                           sequence=sequence,ack_number=self.ack)

        # send the packet
        self.trace("%s (%d) sending TCP segment to %d for %d" % (self.node.hostname,self.source_address,self.destination_address,packet.sequence))
        self.transport.send_packet(packet)

        # set a timer
        if not self.timer:
            self.timer = Sim.scheduler.add(delay=self.rtt, event='retransmit', handler=self.retransmit)
        
        # record when it was sent
        self.add_to_timer(sequence)

    def handle_ack(self,packet):
        ''' Handle an incoming ACK. '''
        self.trace("%s (%d) Incoming ACK received from %d for %d" % (self.node.hostname, packet.destination_address, packet.source_address, packet.ack_number))
        prev_seq = self.sequence
        self.sequence = packet.ack_number
        # increase window by the amount of data acked
        self.increase_window(self.sequence-prev_seq)
        self.send_buffer.slide(packet.ack_number)
        self.recalculate_timeout(packet.sequence)
        if self.send_buffer.outstanding() == 0:
            self.cancel_timer()
            self.send("")
        else:
            self.restart_timer()

    def retransmit(self,event):
        ''' Retransmit data. '''
        self.trace("%s (%d) retransmission fired" % (self.node.hostname,self.source_address))
        self.loss_event()
        self.rtt = 1
        self.dev_rtt = 0
        self.timer = Sim.scheduler.add(delay=self.timeout, event='retransmit', handler=self.retransmit)
        (data, i) = self.send_buffer.resend(1000)
        self.send_packet(data, i)
        self.remove_from_timer(i)

    def cancel_timer(self):
        ''' Cancel the timer. '''
        if not self.timer:
            return
        Sim.scheduler.cancel(self.timer)
        self.timer = None

    def restart_timer(self):
        ''' Cancel the timer & create a new one. '''
        if self.timer:
            Sim.scheduler.cancel(self.timer)
            self.timer = None
        self.timer = Sim.scheduler.add(delay=self.rtt, event='retransmit', handler=self.retransmit)

    def recalculate_timeout(self, packet_num):
        time_between = self.remove_from_timer(packet_num)
        if time_between == -1:
            self.rtt = self.timeout
        else:
            est = (1-self.alpha)*self.rtt + self.alpha*time_between
            self.rtt = min(max(self.min_rtt, est), self.timeout)

    def add_to_timer(self, packet_num):
        self.packet_times[packet_num] = time.time()

    def remove_from_timer(self, packet_num):
        try:
            diff = time.time() - self.packet_times[packet_num]
            del self.packet_times[packet_num]
            return diff
        except KeyError:
            return -1

    def loss_event(self):
        self.threshold = max(self.window/2, self.mss)
        self.window = 1 * self.mss

    # slow start & AI
    def increase_window(self, amount):
        # loss event check
        self.duplicates += 1
        if amount == 0 and self.duplicates >= 4:
            self.loss_event()
        else:
            self.duplicates = 0

            # AI
            if amount + self.window >= self.threshold:
                self.window += (self.mss * amount / self.window)
                self.threshold = self.window
            # slow start
            else:
                self.window += amount


    ''' Receiver '''

    def handle_data(self,packet):
        ''' Handle incoming data. This code currently gives all data to
            the application, regardless of whether it is in order, and sends
            an ACK.'''
        self.trace("%s (%d) received TCP segment from %d for %d (%d)" % (self.node.hostname,packet.destination_address,packet.source_address,packet.sequence,packet.source_port))
        self.receive_buffer.put(packet.body, packet.sequence)
        (data,start) = self.receive_buffer.get()
        self.app.receive_data(data)
        self.ack = start + len(data)
        self.send_ack(packet.sequence)

    def send_ack(self, old_seq):
        ''' Send an ack. '''
        packet = TCPPacket(source_address=self.source_address,
                           source_port=self.source_port,
                           destination_address=self.destination_address,
                           destination_port=self.destination_port,
                           sequence=old_seq,ack_number=self.ack)
        # send the packet
        self.trace("%s (%d) sending TCP ACK to %d for %d (%d)" % (self.node.hostname,self.source_address,self.destination_address,packet.ack_number,packet.source_port))
        self.transport.send_packet(packet)
