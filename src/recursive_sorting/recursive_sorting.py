# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    arrA_index = 0
    arrB_index = 0
    merged_index = 0

    while arrA_index < len(arrA) and arrB_index < len(arrB):
        if arrA[arrA_index] <= arrB[arrB_index]:
            merged_arr[merged_index] = arrA[arrA_index]
            arrA_index += 1
        else:
            merged_arr[merged_index] = arrB[arrB_index]
            arrB_index += 1

        merged_index +=1
    
    while arrB_index < len(arrB):
        merged_arr[merged_index] = arrB[arrB_index]
        arrB_index += 1
        merged_index += 1

    while arrA_index < len(arrA):
        merged_arr[merged_index] = arrA[arrA_index]
        arrA_index += 1
        merged_index += 1   

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION.
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        half_index = len(arr) // 2
        left_arr_half = arr[:half_index]
        right_arr_half = arr[half_index:]
        return merge(merge_sort(left_arr_half), merge_sort(right_arr_half))

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    left_half = arr[start:mid]
    right_half = arr[mid:end + 1]
    left_half.append = (999999999)
    right_half.append = (999999999)
    left_index = right_index = 0
    for index in range(start, end + 1):
        if left_half[left_index] <= right_half[right_index]:
            arr[index] = left_half[left_index]
            index += 1
        else: 
            arr[index] = right_half[right_index]
            right_index += 1
            
    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
