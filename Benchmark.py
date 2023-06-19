"""
Benchmarking of functions using randomly generated arrays:
"""
import random
import time
from SorteringsBib import*

def random_arr(n,mini,maxi):
    """Creates an array populated by n random integers"""
    array_size = n
    minimum = mini
    maximum = maxi
    random_array = []

    for x in range(array_size):
        random_integer = random.randint(minimum, maximum)
        random_array.append(random_integer)
    return random_array

def main():
    #Compare speed for large data-set:
    """Benchmark Insertion"""
    Insertion_time = []
    start = time.time()
    Insertion(random_arr(10000,0,1000))
    end = time.time()
    Insertion_time.append(end-start)
    """Benchmark Selection"""
    Selection_time = []
    start = time.time()
    Selection(random_arr(10000,0,1000))
    end = time.time()
    Selection_time.append(end-start)
    """Benchmark Quick"""
    Quick_time = []
    start = time.time()
    Quick(random_arr(10000,0,1000))
    end = time.time()
    Quick_time.append(end-start)
    """Benchmark Count"""
    Count_time = []
    start = time.time()
    Count(random_arr(10000,0,1000))
    end = time.time()
    Count_time.append(end-start)

    assert Count_time < Quick_time
    assert Quick_time < Selection_time
    assert Selection_time < Insertion_time

    #Compare speed for small data-set:
    """Benchmark Insertion"""
    Insertion_time = []
    start = time.time()
    Insertion(random_arr(50,0,1000))
    end = time.time()
    Insertion_time.append(end-start)
    """Benchmark Selection"""
    Selection_time = []
    start = time.time()
    Selection(random_arr(50,0,1000))
    end = time.time()
    Selection_time.append(end-start)
    """Benchmark Quick"""
    Quick_time = []
    start = time.time()
    Quick(random_arr(50,0,1000))
    end = time.time()
    Quick_time.append(end-start)
    """Benchmark Count"""
    Count_time = []
    start = time.time()
    Count(random_arr(50,0,1000))
    end = time.time()
    Count_time.append(end-start)

    assert Insertion_time <= Count_time
    assert Selection_time <= Quick_time
    

    #Compare speed of Count- and Quick-Sort when range > n:
    Count_time = []
    start = time.time()
    Count(random_arr(10000,0,1000000))
    end = time.time()
    Count_time.append(end-start)
    Quick_time = []
    start = time.time()
    Quick(random_arr(10000,0,1000000))
    end = time.time()
    Quick_time.append(end-start)

    assert Quick_time < Count_time
    

if __name__ == '__main__': main()
