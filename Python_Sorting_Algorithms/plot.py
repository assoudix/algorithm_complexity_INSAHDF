#!/usr/bin/python3


import time
import random
import matplotlib.pyplot as plt
from bulle import bulle
from fusion import mergeSort
from insertion import insertion
from selection import selectionSort
from rapide import Rapide

def generate_random_array(size):
    return [random.randint(0, 1000) for _ in range(size)]

def measure_time(algorithm, arr, *args):
    start_time = time.time()
    algorithm(arr, *args)
    end_time = time.time()
    return end_time - start_time

#Agrandir pour des résultats plus fiables

input_sizes = [2000, 4000, 6000, 8000, 10000]

sorting_algorithms = {
    'Bubble Sort': bulle,
    'Merge Sort': mergeSort,
    'Insertion Sort': insertion,
    'Selection Sort': selectionSort,
    'Quick Sort': Rapide
}

for algorithm_name, algorithm in sorting_algorithms.items():
    execution_times = []
    for size in input_sizes:
        arr = generate_random_array(size)
        if algorithm_name in ['Merge Sort', 'Quick Sort']:
            time_taken = measure_time(algorithm, arr, 0, len(arr) - 1)
        elif algorithm_name == 'Selection Sort':
            time_taken = measure_time(algorithm, arr, size)
        else:
            time_taken = measure_time(algorithm, arr)
        execution_times.append(time_taken)
    plt.plot(input_sizes, execution_times, label=algorithm_name)

plt.xlabel('Input Size')
plt.ylabel('Time (s)')
plt.title('Sorting Algorithm Efficiency')
plt.legend()

plt.savefig('sorting_algorithms_efficiency.png')

print("Plot saved as 'sorting_algorithms_efficiency.png'")
