def myzip(it1, it2):
    """
    Custom implementation of the zip function for two collections.

    Args:
    it1 (iterable): The first iterable to be zipped.
    it2 (iterable): The second iterable to be zipped.

    Returns:
    list of tuples: A list of tuples, each containing elements from both iterables.
    """
    zipped_result = []
    min_len = min(len(it1), len(it2))

    for i in range(min_len):
        zipped_result.append((it1[i], it2[i]))

    return zipped_result

# Test the myzip function
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

zipped_result = myzip(list1, list2)
print(f"Zipped result: {zipped_result}")
