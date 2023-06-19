# Sorteringsbibliotek
This library provides a collection of four sorting algorithms for use in Python 3.7.

A sorting algorithm is an algorithm that puts elements of a list in order. These four algorithms sorts in numerical or alphabetical depending on the type of the elements of the list. 

This library can only handle arrays with elements of the same type, eg [int, int, int] works fine but [int, str, int] will not work. The input is always an array and the output will always be that same array but sorted.
Different algorithms are best suited for arrays of different length and with different elements, thus this library aims to provide a variety of choices depending on the users needs. 

The library consists of the following sorting algorithms: 

1. **Insertion Sort:**
    In-place algorithm that works by splitting the array into a sorted and an unsorted part. Elements from the unsorted part are
    chosen and placed at the correct position in the sorted part. It is efficient for small- to medium-sized data-sets.
    
    ```
    def Insertion(a):
        #Input: Array consisting of elements of the same type
        #Output: The same array but sorted
    ```
    [Further reading](https://en.wikipedia.org/wiki/Insertion_sort)

2. **Selection Sort**:
    In-place algorithm that works by repeatedly choosing the smallest element from unsorted part of the array and moving it
    to the sorted part. This algorithm is efficient for small-sized data-sets.
    
    ```
    def Selection(a):
        #Input: Array consisting of elements of the same type
        #Output: The same array but sorted
    ```
    [Further reading](https://en.wikipedia.org/wiki/Selection_sort)

3. **Quick Sort**:
    Works by recursivley dividing the array using a pivot, the pivot is chosen at random (using Python's 
    built-in random module) in order to effectivize the choice of pivot. Smaller elements are placed to the 
    left of the pivot and larger to the right. This algorithm is efficient for large-sized data-sets.
    
    ```
    def Quick(a):
        #Input: Array consisting of elements of the same type
        #Output: The same array but sorted
    ```
    [Further reading](https://en.wikipedia.org/wiki/Quicksort)
    
    [Random Module](https://docs.python.org/3/library/random.html)

4. **Count Sort**:
    Only works for non-negative integers. It counts the number of occurances of each element in the array,
    thus determining the correct order based on the frequency of each element.
    This algorithm is efficient for arrays whose range is <= the number of elements.
    
    ```
    def Count(a):
        #Input: Array consisting of non-negative integers
        #Output: The same array but sorted
    ```
    [Further reading](https://en.wikipedia.org/wiki/Counting_sort)
