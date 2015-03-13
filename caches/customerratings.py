#!/usr/bin/env python

import sys
import urllib
import re
import numpy

def start():
    customer_ratings_hash = {}
    start = 1
    end = 17771
    i = start
    while(i < end):
        url = 'http://www.cs.utexas.edu/users/downing/netflix/training_set/mv_' + str(i).zfill(7) + '.txt'
        z = urllib.urlopen(url)
        for line in z:
            s = re.split(',', line)
            if len(s) > 1 :
                if s[0] in customer_ratings_hash:
                    a = customer_ratings_hash[s[0]]
                    a += [int(s[1])]
                    customer_ratings_hash.update({s[0]: a})
                else:
                    customer_ratings_hash.update({s[0]: [int(s[1])]})
        print(i)
        i += 1
    
    customer_ratings = {}
    for item in customer_ratings_hash:
        average = numpy.average(customer_ratings_hash[item])
        t = "%.2f" % average
        customer_ratings.update({item: t})

    f = file('customer_ratings.txt', 'wt')
    f.write(str(customer_ratings))

start()
