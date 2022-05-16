from unittest.util import sorted_list_difference


def bubble_sort(unsorted_list):
    n = len(unsorted_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if unsorted_list[j] > unsorted_list[j+1]:
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]

unsorted_list = [9,8,7,6,5,4,3,2,1]

bubble_sort(unsorted_list)
print(unsorted_list)

