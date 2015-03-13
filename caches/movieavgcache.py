#!/usr/bin/env python

import sys
import urllib
import numpy
import re

def start():
    cache = {}
    start = 1
    end = 17771
    while(start < end):
        url = 'http://www.cs.utexas.edu/users/downing/netflix/training_set/mv_' + str(start).zfill(7) + '.txt' 
        z = urllib.urlopen(url)
        list = []
        for line in z:
            s = re.split(',', line)
            if len(s) > 1:
                list += [int(s[1])]
        cache.update({start: list})
        print(start)
        start += 1

    finalcache = {}
    for item in cache:
        average = numpy.average(cache[item])
        t = "%.2f" % average
        finalcache.update({item: t})
    f = file('movieaverage.txt', 'wt')
    f.write(str(finalcache))

start()
