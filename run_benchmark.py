import random
import time
import csv


# =====================================================
# SORTING ALGORITHMS
# =====================================================

def bubble_sort(arr):

    a = arr.copy()

    n = len(a)

    for i in range(n):

        for j in range(0, n - i - 1):

            if a[j] > a[j + 1]:

                a[j], a[j + 1] = a[j + 1], a[j]

    return a


def insertion_sort(arr):

    a = arr.copy()

    for i in range(1, len(a)):

        key = a[i]

        j = i - 1

        while j >= 0 and a[j] > key:

            a[j + 1] = a[j]

            j -= 1

        a[j + 1] = key

    return a


def selection_sort(arr):

    a = arr.copy()

    n = len(a)

    for i in range(n):

        min_idx = i

        for j in range(i + 1, n):

            if a[j] < a[min_idx]:

                min_idx = j

        a[i], a[min_idx] = a[min_idx], a[i]

    return a


def shell_sort(arr):

    a = arr.copy()

    n = len(a)

    gap = n // 2

    while gap > 0:

        for i in range(gap, n):

            temp = a[i]

            j = i

            while j >= gap and a[j - gap] > temp:

                a[j] = a[j - gap]

                j -= gap

            a[j] = temp

        gap //= 2

    return a


def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])

    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):

    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:

            result.append(left[i])

            i += 1

        else:

            result.append(right[j])

            j += 1

    result.extend(left[i:])

    result.extend(right[j:])

    return result


def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]

    middle = [x for x in arr if x == pivot]

    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


def heapify(a, n, i):

    largest = i

    left = 2 * i + 1

    right = 2 * i + 2


    if left < n and a[left] > a[largest]:

        largest = left


    if right < n and a[right] > a[largest]:

        largest = right


    if largest != i:

        a[i], a[largest] = a[largest], a[i]

        heapify(a, n, largest)



def heap_sort(arr):

    a = arr.copy()

    n = len(a)


    # BUILD MAX HEAP

    for i in range(n // 2 - 1, -1, -1):

        heapify(a, n, i)


    # EXTRACT ELEMENTS

    for i in range(n - 1, 0, -1):

        a[i], a[0] = a[0], a[i]

        heapify(a, i, 0)


    return a


def counting_sort(arr, exp):

    n = len(arr)

    output = [0] * n

    count = [0] * 10

    for i in arr:

        index = i // exp

        count[index % 10] += 1

    for i in range(1, 10):

        count[i] += count[i - 1]

    i = n - 1

    while i >= 0:

        index = arr[i] // exp

        output[count[index % 10] - 1] = arr[i]

        count[index % 10] -= 1

        i -= 1

    for i in range(n):

        arr[i] = output[i]


def radix_sort(arr):

    a = arr.copy()

    exp = 1

    max_num = max(a)

    while max_num // exp > 0:

        counting_sort(a, exp)

        exp *= 10

    return a


# =====================================================
# DATA GENERATORS
# =====================================================

def generate_random(n):

    return [random.randint(1, 100000) for _ in range(n)]


def generate_sorted(n):

    return list(range(n))


def generate_reversed(n):

    return list(range(n, 0, -1))


def generate_nearly_sorted(n):

    arr = list(range(n))

    for _ in range(n // 20):

        i = random.randint(0, n - 1)

        j = random.randint(0, n - 1)

        arr[i], arr[j] = arr[j], arr[i]

    return arr


# =====================================================
# CONFIG
# =====================================================

algorithms = {

    "Bubble Sort": bubble_sort,
    "Insertion Sort": insertion_sort,
    "Selection Sort": selection_sort,

    "Shell Sort": shell_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
    "Heap Sort": heap_sort,

    "Radix Sort": radix_sort,

    "TimSort": sorted
}


test_cases = {

    "Random": generate_random,
    "Sorted": generate_sorted,
    "Reversed": generate_reversed,
    "Nearly Sorted": generate_nearly_sorted
}


sizes = [

    100,
    250,
    500,
    1000,
    2500,
    5000,
    7500,
    10000,
    15000,
    20000
]


# =====================================================
# BENCHMARK
# =====================================================

with open("results.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([

        "Algorithm",
        "Case",
        "Input Size",
        "Execution Time"

    ])

    for case_name, generator in test_cases.items():

        print(f"\n=== {case_name} ===")

        for size in sizes:

            print(f"\nInput Size: {size}")

            data = generator(size)

            for alg_name, alg_func in algorithms.items():

                start = time.perf_counter()

                alg_func(data)

                end = time.perf_counter()

                execution_time = end - start

                print(
                    f"{alg_name:<20} {execution_time:.6f} sec"
                )

                writer.writerow([

                    alg_name,
                    case_name,
                    size,
                    execution_time

                ])

print("\nBenchmark completed.")