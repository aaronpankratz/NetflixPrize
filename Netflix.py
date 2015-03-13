#!/usr/bin/env python

import sys
import math
import numpy

def Netflix_main(r,w,l,probe):
    """""
    # Netflix_solve
    # Takes a given input probe file and calculates prediction ratings for every customer
    # parameters: input Probe file, file to write output to, actual ratings, and boolean for output
    # returns: nothing, but writes to the given output file
    """""

    # initialize dictionary caches
    f = open('caches/movieaverage.txt', 'r')
    movieavgcache = eval(f.read())
    f = open('caches/customer_ratings.txt', 'r')
    customerratingcache = eval(f.read())

    # initialize other variables
    totalrecords = 0
    a = 0.0
    RMSE = 0.0
    actualvalue = l
    xyz = numpy.average(actualvalue)
    listforcalc = []
    listforprint = []
    list2forcalc = []
    counter = 0

    # step through each line of the input file
    for line in r :
        totalrecords += 1
        s = line.split(':')
        # this determines if the line is a movie id or customer id
        if len(s) > 1 :

            # movie id, get the movie average from cache
            a = float(movieavgcache[int(s[0])])
            listforprint += [s[0]+ ':\n']
        else :
            #end of line, for RunNetflix.in
            if s[0] == '\n':

                # calculate RMSE
                RMSE = Netflix_RMSE(listforcalc, list2forcalc)

                # write to output file
                w.write(str(RMSE)+ '\n')
                for line in listforprint:
                    w.write(line)
                w.write(str(totalrecords) + ' records total\n')
                listforcalc = []
                listforprint = []
                list2forcalc = []
            else:

                # customer id, get the customer average from cache
                b = float(customerratingcache[s[0].strip('\n')])

                # calculate the prediction
                # Overall average movie rating + (Customer average rating - Overall average rating)
                calculation = a + (b - xyz)
                strcalc = "%.2f" % calculation
                listforprint += [strcalc + '\n']
                listforcalc += [float(strcalc)]
                list2forcalc += [actualvalue[counter]]
                counter += 1

    # if outputting to ProbeNetflix.out
    if probe:

        # calculate RMSE
        RMSE = Netflix_RMSE(listforcalc, list2forcalc)

        # write to output file
        w.write(str(RMSE)+ '\n')
        for line in listforprint:
            w.write(line)
        w.write(str(totalrecords) + ' records total\n')

def sqre_diff (x, y) :
    """""
    # sqre_diff
    # calculates the squared difference of the two input values
    # parameters: two floats: x, y
    # returns: (x - y)^2
    """""
    return (x - y) ** 2

def Netflix_RMSE(a, p):
    """""
    # Netflix_RMSE
    # calculates the RMSE between two lists
    # parameters: two lists
    # returns: float value representation of the RMSE
    """""
    assert len(a) == len(p)
    assert len(a) != 0
    s = len(a)
    v = sum(map(sqre_diff, a, p), 0.0)
    assert v >= 0
    return math.sqrt(v / s)
