B = [10, 14, 19, 26, 27, 31, 33, 35, 42, 44]


# insertion sort
def insertionSort(A):
    for i in range(len(A) - 1):
        min = i
        j = i + 1
        for j in range(i + 1, len(A)):
            if A[min] > A[j]:
                min = j
        A[i], A[min] = A[min], A[i]

    return A


# Binary search

def binarySearch(arr, low, high, target):
    mid = low + (high - low) / 2
    while high > low:
        if arr[int(mid)] == target:
            return arr[int(mid)]
        elif arr[int(mid)] > target:
            high = mid - 1
            return binarySearch(arr, low, high, target)
        elif arr[int(mid)] < target:
            low = mid + 1
            return binarySearch(arr, low, high, target)

    return False


exArray = [10, 15, 3, 7]
insertionSort(exArray)
print(exArray)


def findCombination(arr, total):
    for x in arr:
        other = total - x
        if binarySearch(arr, 0, len(arr) - 1, other):
            return x, binarySearch(arr, 0, len(arr) - 1, other)


print(findCombination(exArray, 22))
