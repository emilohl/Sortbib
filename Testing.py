"""
Testing of functions:
"""
import random
from SorteringsBib import*

def main():
    #Test of empty array as input:
    a = []
    
    assert Insertion(a) == []
    assert Selection(a) == []
    assert Quick(a) == []
    assert Count(a) == []
    
    #Test of repeated elements:
    exp = [1, 2, 2, 3, 4, 5]
    
    a = [5, 4, 2, 3, 2, 1]
    assert Insertion(a) == exp
    a = [5, 4, 2, 3, 2, 1]
    assert Selection(a) == exp
    a = [5, 4, 2, 3, 2, 1]
    assert Quick(a) == exp
    a = [5, 4, 2, 3, 2, 1]
    assert Count(a) == exp

    #Test of strings:
    exp = ['a', 'c', 'd', 'e', 'h']
    
    a = ['c', 'e', 'a', 'h', 'd']
    assert Insertion(a) == exp
    a = ['c', 'e', 'a', 'h', 'd']
    assert Selection(a) == exp
    a = ['c', 'e', 'a', 'h', 'd']
    assert Quick(a) == exp
    a = ['c', 'e', 'a', 'h', 'd']
    assert Count(a) == 'only non-negative integers allowed'

    #Test of negative integers:
    exp = [-1, 0, 1, 2]
    
    a = [2, 0, -1, 1]
    assert Insertion(a) == exp
    a = [2, 0, -1, 1]
    assert Selection(a) == exp
    a = [2, 0, -1, 1]
    assert Quick(a) == exp
    a = [2, 0, -1, 1]
    assert Count(a) == 'only non-negative integers allowed'
    
if __name__ == '__main__': main()
