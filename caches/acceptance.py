
import sys
import urllib
import random

def start():
    
    f = open('RunNetflix.in', 'wt')
    g = file('acceptance_actual_ratings.txt', 'wt')
    i = 0
    while i < 100:
        x = 0
        while x < 1000:
            start = 1
            end = int(random.random()*100)+1

            movie = int(random.random()*17771)
            url = 'http://www.cs.utexas.edu/users/downing/netflix/training_set/mv_' + str(movie).zfill(7) + '.txt'
            y = urllib.urlopen(url)

            f.write(str(movie) + ':\n')
            g.write(str(movie) + ':\n')
            while start < end:
                a = y.readline()
                a = a.split(',')
                if len(a) > 2:
                    f.write(str(a[0]) + '\n')
                    g.write(str(int(a[1])) + '\n')
                start += 1

            x += end
        f.write('\n')
        i += 1

start()
