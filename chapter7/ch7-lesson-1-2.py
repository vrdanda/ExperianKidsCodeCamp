def linear_search(arr, target):
    """
    Performs linear search to find the target element in the given list.
    Args:
        arr (list): The list to search.
        target: The element to search for.
    Returns:
        int: The index of the target element if found, else -1.
    """
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1

# Example usage​
my_list = [40, 50, 10, 20, 30, 100]
target_element = 30

result = linear_search(my_list, target_element)
if result != -1:
    print(f"Element {target_element} found at index {result}.")
else:
    print(f"Element {target_element} not found in the list.")