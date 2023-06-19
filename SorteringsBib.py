"""
This is a library consisting of common sorting algorithms. A pre-requisite for use is that all elements
in the input of the array are the same type.
"""
import random

def Insertion(a):
    """
    An 'Insertion Sort' function that returns the elements of the array in sorted (ascending) order. 
    Time-complexity O(n^2).
    """
    for i in range(1,len(a)):
        curr = a[i]
        j = i-1
        while j>=0 and a[j] > curr:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = curr
    return a

def Selection(a):
    """
    A 'Selection Sort' function that returns the elements of the array in sorted (ascending) order.
    In place algorithm with time-complexity O(n^2).
    """   
    for i in range(len(a)):
        min_element = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_element]:
                min_element = j               
        a[i], a[min_element] = a[min_element], a[i]
    return a

def Quick(a):
    """
    A 'Quick Sort' function that returns the elements of the array in sorted (ascending) order.
    Time-Complexity O(1,4*n*logn).
    """
    if len(a) <= 1:
        return a
    pivot = random.choice(a)
    small = [x for x in a if x < pivot]
    equal = [x for x in a if x == pivot]
    large = [x for x in a if x > pivot]
    a = Quick(small) + equal + Quick(large)
    return a

def Count(a):
    """
    A 'Count sort' function returns the elements, non-negative integers, of the array in
    sorted (ascending) order.
    Time complexity O(n+k), linear time complexity if k = S*n where S is a constant > 0.
    """
    if len(a) <= 1:
        return a
    if type(max(a)) == int:
        count = [0]*(max(a)+1)              
        sort = [0]*len(a)
    else:
        return 'only non-negative integers allowed'                

    for n in a:
        count[n] += 1
        if n < 0:
            return 'only non-negative integers allowed'
        
    for i in range(1, len(count)):
        count[i] += count[i-1]          

    for i in range(len(a)-1, -1, -1):
        sort[count[a[i]]-1] = a[i]      
        count[a[i]] -= 1

    for i in range(0,len(a)):
        a[i] = sort[i]
    return a

    
def main():
    """"""
if __name__ == '__main__': main()
