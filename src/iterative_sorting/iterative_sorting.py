# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for smallest_index in range (cur_index + 1, len(arr)):
            if arr[smallest_index] < arr[cur_index]:
                cur_index = smallest_index             

        # TO-DO: swap
        if smallest_index != i:
            arr[i], arr[cur_index] = arr[cur_index], arr[i]
            
    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(0, len(arr) - 1):
        for second_index in range(0, len(arr) - 1 - i):
            if arr[second_index] > arr[second_index + 1]:
                arr[second_index], arr[second_index + 1] = arr[second_index + 1], arr[second_index]
                
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr