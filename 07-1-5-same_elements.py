def same_set(a, b):
    return set(a) == set(b)

# Example usage:
list1 = [1, 4, 9, 16, 9, 7, 4, 9, 11]
list2 = [11, 11, 7, 9, 16, 4, 1]
print(same_set(list1, list2)) 