import sys

def start():
    f = open('acceptance_actual_ratings.txt', 'r')
    w = file('acceptancearlist.txt', 'wt')
    list = []
    for line in f:
        s = line.split(':')
        if len(s) < 2:
            list += [float(s[0].strip('\n'))]
    w.write(str(list))

start()
