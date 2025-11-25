def binary_search(array, target):
    low, high = 0, len(array) - 1
    mid = (low + high) // 2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search(array[mid + 1:], target) + mid + 1
    elif array[mid] > target:
        return binary_search(array[:mid], target)
    return -1

def main():
    array = [1, 4, 5, 6, 9, 10, 24, 43, 54, 55, 65]
    target = 10
    index = binary_search(array, target)
    print(f"Target: {target} was found at index {index}")

if __name__ == "__main__":
    main()
