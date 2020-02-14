from typing import List

# Returns a new list, where each element i is a[i] + b[i]
def list_sums(a : List[int], b : List[int]) -> List[int]:
    newList = []
    # TODO: Finish this implementation
    for x, y in zip(a,b):
        newList.append(x + y) # Why does this seem off? 
    return newList

first_list  = [1,2,3]
second_list = [2,3,1]

print("Sum of {0} and {1} is {2}".format(first_list, second_list, list_sums(first_list, second_list)))
