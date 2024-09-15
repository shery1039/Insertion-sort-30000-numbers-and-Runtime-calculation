# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 00:49:18 2024

@author: hp
"""

import random
import time
import csv

from BubbleSort import randomArray  # Assuming this is where your randomArray function is defined

def InsertionSort(array, start, end):
    """Sort the array using the insertion sort algorithm."""
    for i in range(start + 1, end):
        temp = array[i]
        j = i - 1
        while j >= start and temp < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = temp

# Generate a random array of 30,000 integers
size = 30000
random_numbers = randomArray(size)

print(f"Generated random array of size {size}.")

print("Random Array: ", random_numbers) 

# Measure the runtime of the InsertionSort function
start_time = time.time()
InsertionSort(random_numbers, 0, size)
end_time = time.time()
Run_time = end_time - start_time

# Print the entire sorted array
print("Sorted Array: ", random_numbers)

# Print the runtime
print("Run time is", Run_time, "seconds")

# Save the sorted array to a CSV file
with open("SortedInsertionSort.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Sorted Array"])
    for number in random_numbers:
        writer.writerow([number])
