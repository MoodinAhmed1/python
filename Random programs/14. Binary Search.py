# Binary Search

# Implement the binary search algorithm on a sorted list.

# Example: list = [1, 3, 5, 7, 9], target=5 → Found at index 2

def search(array, target):
    high = len(array) - 1
    low = 0

    while low <= high:
        mid = (high + low) // 2

        if target == array[mid]:
            return mid
        elif target < array[mid]:
            high = mid - 1
        else:
            low = mid + 1
            
    return -1

print(search([1, 3, 5, 7, 9], 9))
print(search([1, 3, 5, 7, 9], 10))
            
            
# recursive method
# def search(array, target, low = 0, high = None):
    
#     if high is None:
#         high = len(array) - 1
    
#     if low > high:
#         return -1
        
#     midIndex = len(array) // 2
#     mid = array[midIndex]
    
#     if target == mid:
#         return midIndex
    
#     if target < mid:
#         search(array, target, low, midIndex)
#     else:
#         search(array, target, midIndex, high)
    

# print(search([1, 3, 5, 7, 9], target=5))