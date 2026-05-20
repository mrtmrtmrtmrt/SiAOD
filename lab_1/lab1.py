import time
import random

def find_elem_in_arr(arr,target):
    for i in arr:
        if i == target:
            return True
    return False

def find_second_max_in_arr(arr):
    max1 = arr[0]
    max2 = arr[0]
   
    for i in range(len(arr)):
        if arr[i] > max1:
            max2 = max1
            max1 = arr[i]
        elif (max2 < max1) and (arr[i] > max2):
            max2 = arr[i]
    return max2
             
def binary_search(arr,target):
    left_index = 0
    right_index = len(arr)
    while left_index < right_index:
        middle_index = left_index + (right_index - left_index) // 2
        if arr[middle_index] < target:
            left_index = middle_index + 1
        else:
            right_index = middle_index
    return left_index
def create_multiplication_table(n):
    table = []
    for i in range(1, n+1):
        row = []
        for j in range(1, n+1):
            row.append(i * j)
            #print(i*j, e#d="\t")
        #print()
        table.append(row)
    return table



def generate_array(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 10000))
    return arr

def generate_sorted_array(n):
    arr = []
    for i in range(n):
        arr.append(i)
    return arr

def measure_time_one_arg(func, data):
    start = time.perf_counter()
    func(data)
    end = time.perf_counter()
    return end - start

def measure_time_two_args(func, data, target):
    start = time.perf_counter()
    func(data,target)
    end = time.perf_counter()
    return end - start


if __name__ == '__main__':
    print("n       find_elem_in_arr        find_second_max_in_arr  binary_search           n//100  create_multiplication_table(n//100)")
    sizes = [150000, 250000, 500000, 1000000]
    for n in sizes:
        arr = generate_array(n)
        sortedarr = generate_sorted_array(n)
        target = random.randint(0,n-1)
        #print("n       find_elem_in_arr        find_second_max_in_arr  binary_search            n//100      create_multiplication_table")
        time_find_second_max_in_arr = measure_time_one_arg(find_second_max_in_arr, arr)
        time_find_elem_in_arr = measure_time_two_args(find_elem_in_arr,arr,target)
        time_binary_search = measure_time_two_args(binary_search,sortedarr,target)
        time_create_multiplication_table = measure_time_one_arg(create_multiplication_table,(n//100))

        print(n, time_find_elem_in_arr, time_find_second_max_in_arr, time_binary_search, (n//100), time_create_multiplication_table, sep="\t")