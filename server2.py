# -*- coding: cp936 -*-

from SocketServer import TCPServer,StreamRequestHandler
#from SocketServer import ForkingMixIn#分叉,windows系统不支持
from SocketServer import ThreadingMixIn#多线程


#class Server(ForkingMixIn,TCPServer):pass#分叉,windows系统不支持
class Server(ThreadingMixIn,TCPServer):pass#多线程

class Handler(StreamRequestHandler):
    def handle(self):
        addr=self.request.getpeername()
        print 'Got connection from',addr
        self.wfile.write('Thank you for connecting')

server=Server(('',12345),Handler)
server.serve_forever()
