#!/usr/bin/python3

def selectionSort(array, size):
    """Selection sort implementation on Python - Quadratic complexity - Omar Assoudi"""
    for index in range(size):
        small_index = index

        for j in range(index + 1, size):
            if array[j] < array[small_index]:
                small_index = j
        (array[index], array[small_index]) = (array[small_index], array[index]) #swap