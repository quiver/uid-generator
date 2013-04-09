# vim: set fileencoding=utf8
'''XML-RPC server for 8-character unique id generator
'''
import argparse
from SimpleXMLRPCServer import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
import uid

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

class IdGenMethod(object):
    def __init__(self, db):
        self.uid = uid.UIDGenerator(db=db)

    def id(self):
        return self.uid.id()
    
    def counter(self):
        return self.uid.counter()
    
    def reset(self):
        return self.uid.reset()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, nargs='?', default=8000)
    parser.add_argument('--db', type=int, nargs='?', default=0)
    args =  parser.parse_args()

    # Create server
    server = SimpleXMLRPCServer(("localhost", args.port),
                                requestHandler=RequestHandler,
                                allow_none=True)
    server.register_introspection_functions()
    server.register_instance(IdGenMethod(args.db))
    server.serve_forever()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
