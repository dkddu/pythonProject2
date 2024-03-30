def binary_search(list,item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low+high)//2
        guess = list[mid]
        if guess == item:
            return guess
            break
        elif guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return None
my_list = binary_search([1,3,5,7,8,9,12,13],8)
print(my_list)