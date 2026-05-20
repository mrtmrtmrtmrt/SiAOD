import time
import random
import sys

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Сдвигаем элементы, которые больше key, на одну позицию вправо
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def generate_array(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 10000))
    return arr

def measure_time(func, data):
    start = time.perf_counter()
    func(data)
    end = time.perf_counter()
    return end - start

def measure_memory(sort_func, arr):
    test_array = arr.copy()
    
    memory_before = sys.getsizeof(test_array)
    for element in test_array:
        memory_before = memory_before + sys.getsizeof(element)
    
    sort_func(test_array)
    
    memory_after = sys.getsizeof(test_array)
    for element in test_array:
        memory_after = memory_after + sys.getsizeof(element)
    return memory_before, memory_after

if __name__ == "__main__":
    sizes = [100, 500, 1000, 2000, 5000]
    print("size    Время(с)                Память до (байт)        Память после (байт)")
    for n in sizes:
        arr = generate_array(n)
        
        time_table = measure_time(insertion_sort, arr.copy())
        memory_before, memory_after = measure_memory(insertion_sort, arr)
        
        print(n, time_table, memory_before,"\t", memory_after, sep="\t")    