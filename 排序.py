def smallest_number(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
def rank_number(list):
    new_arr = []
    for i in range(len(list)):
         smallest_numbe = smallest_number(list)
         new_arr.append(list.pop(smallest_numbe))
    return new_arr
new_arr = rank_number([1,3,6,4,5])
print(new_arr)

