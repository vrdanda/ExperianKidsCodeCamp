def binary_search(sorted_list, target):
    """
    Performs binary search to find the target element in the given sorted list.
    Args:
        sorted_list (list): The sorted list to search.
        target: The element to search for.
    Returns:
        int: The index of the target element if found, else -1.
    """
    left, right = 0, len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
# Example usage​
my_sorted_list = ["apple", "banana", "cherry", "grape", "kiwi", "lemon", "mango", "orange", "peach", "pear",
                  "pineapple", "plum", "raspberry", "strawberry", "tangerine", "watermelon", "blueberry", "fig", "grapefruit", "lime"]
target_word = "kiwi"
result = binary_search(my_sorted_list, target_word)
if result != -1:
    print(f"Word '{target_word}' found at index {result}.")
else:
    print(f"Word '{target_word}' not found in the list.")