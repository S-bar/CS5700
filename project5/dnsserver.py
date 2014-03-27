import getopt
import SocketServer
import struct
import sys
"""
DNS Header
0  1  2  3  4  5  6  7  8  9  0  1  2  3  4  5  6
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
|                       ID                      |
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
|QR| Opcode |AA|TC|RD|RA|    Z   |     RCODE    |
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
|                    QDCOUNT                    |
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
|                    ANCOUNT                    |
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
|                    NSCOUNT                    |
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
|                    ARCOUNT                    |
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
DNS Query
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
/                      QNAME                    /
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
|                      QTYPE                    |
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
|                      QCLASS                   |
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
DNS Answer
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
/                       NAME                    /
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
|                       TYPE                    |
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
|                      CLASS                    |
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
|                       TTL                     |
|                                               |
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
|                     RDLENGTH                  |
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--|
/                      RDATA                    /
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
"""

class DNSPacket:

    def __init__(self):
        self.id = 0

    def build(self):
        packet = struct.pack('H', self.id)
        return packet

    def rebuild(self, raw_packet):
        [self.id] = struct.unpack('H', raw_packet)

port=0
name=''

if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:],'p:n:')

    for o, a in opts:
        if o == '-p':
            port = a
        elif o == '-n':
            name = a
        else:
            print 'Usage: %s -p <port> -n <name>' % sys.argv[0]