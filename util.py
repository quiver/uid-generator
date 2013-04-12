# vim: set fileencoding=utf8

import itertools
import random
import string

def get_shuffled_chars():
    "shuffle characters consisted of lower letters and digits"
    chars = string.ascii_letters + string.digits
    base = [(c1, c2) for c2 in chars for c1 in chars]
    random.shuffle(base)
    return base

def grouper(n, iterable, fillvalue=None):
    # http://stackoverflow.com/a/4170456
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.izip_longest(fillvalue=fillvalue, *args)
