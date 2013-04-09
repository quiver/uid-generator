# vim: set fileencoding=utf8
'''XML-RPC client for id-generator
'''
import argparse
from xmlrpclib import ServerProxy

def test():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', type=str, nargs='?', default='localhost')
    parser.add_argument('--port', type=int, nargs='?', default=8000)
    args = parser.parse_args()
    server = ServerProxy('http://%s:%d' % (args.host, args.port))

    print 'reset'
    server.reset()
    print 'coutner:', server.counter()
    print 'generate 5 ids'
    for i in range(5):
        print server.id()
    print 'coutner:', server.counter()

    print 'generate another 5 ids'
    for i in range(5):
        print server.id()
    print 'coutner:', server.counter()

    print 'reset'
    server.reset()
    print 'coutner:', server.counter()
    print 'generate 3 ids'
    for i in range(3):
        print server.id()
    print 'coutner:', server.counter()

if __name__ == '__main__':
    test()
