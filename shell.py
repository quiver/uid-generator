# vim: set fileencoding=utf8
'''XML-RPC shell client for id-generator
'''

import argparse
import cmd
from xmlrpclib import ServerProxy

class Cmd(cmd.Cmd):
    def __init__(self, host, port, *args, **kw):
        cmd.Cmd.__init__(self, *args, **kw)
        self.prompt = '%s:%d> ' % (host, port)
        self.server = ServerProxy('http://%s:%d' % (host, port))

    def do_id(self, arg):
        result = self.server.id()
        print result

    def do_counter(self, arg):
        result = self.server.counter()
        print result

    def do_reset(self, arg):
        result = self.server.reset()
        print result

    def do_EOF(self, arg):
        return True

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', type=str, nargs='?', default='localhost')
    parser.add_argument('--port', type=int, nargs='?', default=8000)
    args =  parser.parse_args()

    cmd = Cmd(args.host, args.port)
    cmd.cmdloop()

if __name__ == '__main__':
    main()
