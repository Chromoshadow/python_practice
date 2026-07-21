def count_in_list(lst: list, target: any) -> int:
    """Return the count of the target element in the list"""
    count = 0
    for elem in lst:
        if elem == target:
            count += 1
    return count

# print(count_in_list.__doc__)

# print(count_in_list(["toto", "tata", "toto"], "toto")) # output: 2
# print(count_in_list(["toto", "tata", "toto"], "tutu")) # output: 0
