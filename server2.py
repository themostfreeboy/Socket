# -*- coding: cp936 -*-

from SocketServer import TCPServer,StreamRequestHandler
#from SocketServer import ForkingMixIn#�ֲ�,windowsϵͳ��֧��
from SocketServer import ThreadingMixIn#���߳�


#class Server(ForkingMixIn,TCPServer):pass#�ֲ�,windowsϵͳ��֧��
class Server(ThreadingMixIn,TCPServer):pass#���߳�

class Handler(StreamRequestHandler):
    def handle(self):
        addr=self.request.getpeername()
        print 'Got connection from',addr
        self.wfile.write('Thank you for connecting')

server=Server(('',12345),Handler)
server.serve_forever()
