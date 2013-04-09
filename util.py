# vim: set fileencoding=utf8

import itertools
import random
import string

def get_shuffled_chars():
    "shuffle characters consisted of lower letters and digits"
    base = list((string.ascii_lowercase + string.digits) * 2)
    random.shuffle(base)
    return base

def grouper(n, iterable, fillvalue=None):
    # http://stackoverflow.com/a/4170456
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.izip_longest(fillvalue=fillvalue, *args)
