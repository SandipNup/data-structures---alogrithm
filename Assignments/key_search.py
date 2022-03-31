# Algorithm
"""
KeySearch(A[start...end], key)
problem: Search for the key element in the list of sorted elements by using divide and conquer technique.

input: Matrix (A[start...end]) and key element

Define KeySearch(A[start...end], key)

    if start > end :
        return -1 and exit

    mid = (start + end)/2

    if key = A[mid]:
        return mid and exit

    else:
        if key < A[mid]:
            end = mid -1
            return KeySearch(A[start...end], key)
        elseif key > A[mid]:
            start = mid + 1
            KeySearch(A[start...end], key)
    return -1

"""


def key_search(arr, key, start=1, end=0):
    # print(start, end)

    if end == 0:
        end = len(arr)

    if start > end:
        return -1

    mid = int((start + end)/ 2)

    mid_arr_value = arr[mid]

    if key == mid_arr_value:
        return mid
    
    else:
        if key < mid_arr_value:
            end = mid - 1
            return key_search(arr, key, start, end)
        else:
            # key > mid_arr_value
            start = mid + 1
            return key_search(arr, key, start, end)    


if __name__ == "__main__":
    print(key_search([2,4,6,8,10,16,18,20], 11))
    print(key_search([5, 10 , 15, 20, 25, 44], 44))
    print(key_search([2,4,6,7,9,10,11,14,25], 7))
    print(key_search([2,4,6,8,10,16,18,20, 55,67,89], 67))