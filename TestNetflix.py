#!/usr/bin/env python

# imports
import unittest

from Netflix import Netflix_main, Netflix_RMSE, sqre_diff

# main
class TestNetflix (unittest.TestCase) :
    
    # sqre_diff
    def test_sqre_diff1 (self) :
        a = 0
        b = 0
        c = sqre_diff(a, b)
        self.assert_(c == 0)
        
    def test_sqre_diff2 (self) :
        a = 1
        b = 1
        c = sqre_diff(a, b)
        self.assert_(c == 0)
        
    def test_sqre_diff3 (self) :
        a = 4
        b = 2
        c = sqre_diff(a, b)
        self.assert_(c == 4)
        
    # Netflix_RMSE
    def test_Netflix_RMSE1 (self) :
        a = [1]
        b = [1]
        c = Netflix_RMSE(a, b)
        self.assert_(c == 0)
    def test_Netflix_RMSE2 (self) :
        a = [1, 3, 5, 2]
        b = [2, 4, 4, 1]
        c = Netflix_RMSE(a, b)
        self.assert_(c == 1 )
    def test_Netflix_RMSE3 (self) :
        a = [0, 0, 0]
        b = [0, 0, 0]
        c = Netflix_RMSE(a, b)
        self.assert_(c == 0)

    # Netflix_main
    #def test_Netflix_main1 (self):
        
        
print "TestNetflix.py"
unittest.main()
print "Done"
