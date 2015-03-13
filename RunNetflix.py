#!/usr/bin/env python

#--------------------
# project 3 netflix
# Aaron Pankratz
#--------------------


import sys
import urllib
import time
import select

from Netflix import Netflix_main
# ----
# main
# ----
def main(x, y):
    """""
    # send probe data to Netflix_solve()
    #
    # if calling this program with an input, an output must also be specified
    # otherwise the default input is probefile, and default output is ProbeNetflix.out
    #
    # ex: $ python RunNetflix.py < RunNetflix.in > RunNetflix.out
    #  or $ python RunNetflix.py
    """""
    # default input, output
    url_probe = 'http://www.cs.utexas.edu/users/downing/netflix/probe.txt'
    probefile = urllib.urlopen(url_probe)
    w = open('ProbeNetflix.out', 'w')
    z1 = open('caches/acceptancearlist.txt', 'r')
    z2 = open('caches/arlist.txt', 'r')
    z3 = eval(z1.read())
    z4 = eval(z2.read())
    # check for command line input, output
    if select.select([sys.stdin,],[],[],0.0)[0]:
        s = time.clock()
        Netflix_main(x, y, z3, False)
        t = time.clock()
    else:
        s = time.clock()
        Netflix_main(probefile, w, z4, True)
        t = time.clock()
       
    print "RunNetflix runtime:",(t - s),"seconds"

main(sys.stdin, sys.stdout)
