# vim: set fileencoding=utf8
'''XML-RPC server for 8-character unique id generator

Reference : http://debiancdn.wordpress.com/2013/04/07/%E5%8A%A0%E7%95%91%E3%81%95%E3%82%93%E3%82%A4%E3%83%B3%E3%82%BF%E3%83%93%E3%83%A5%E3%83%BC%EF%BC%9A%E8%A1%9D%E7%AA%81%E3%81%97%E3%81%AA%E3%81%84%E6%96%87%E5%AD%97%E5%88%97%E3%82%92%E4%BD%9C%E3%82%8B/
'''
import redis
import util

class UIDGenerator(object):
    '''unique id generator
    '''
    def __init__(self, db):
        self.r = redis.StrictRedis(db=db)
        self._register_script()

    def _register_script(self):
        src = '''
        -- http://redis.io/commands/eval
        local counter = redis.call('incr', 'random:counter')
        local result = ''
        local tbl = {}
        tbl['1'] = 3793
        tbl['2'] = 3797
        tbl['3'] = 3803
        tbl['4'] = 3821
        for k, v in pairs(tbl) do
            result = result .. redis.call('lindex', 'random:p' .. k, counter % v)
        end
        return result
        '''
        self.r_hash = self.r.register_script(src)

    def id(self):
        return self.r_hash()
    
    def counter(self):
        return self.r.get('random:counter')
    
    def reset(self):
        self.r.set('random:counter', 0)
        for suffix in '1234':
            for chars in util.grouper(2, util.get_shuffled_chars()):
                self.r.lpush('random:p%s'%suffix, ''.join(chars))

