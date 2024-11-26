def sum_array(arr):
    if arr == None or len(arr) == 0:
        return 0

    if len(arr) == 2:
        return 0

    if len(arr) == 1:
        return 0

    highest = max(arr)
    lowest = min(arr)
    arr.remove(highest)
    arr.remove(lowest)
    return (sum(arr))