def binary_search(sorted_array, target_value):
    low = 0
    high = len(sorted_array) - 1
    steps = 1
    while low <= high:
        mid = (low + high) // 2
        guess = sorted_array[mid]
        if guess == target_value:
            print("Steps: {}".format(steps))
            return mid
        elif guess > target_value:
            high = mid -1
        elif guess < target_value:
            low = mid + 1
        else:
            raise Exception
        steps += 1




if __name__ == "__main__":
    dummy_array = list(range(15))
    target_index = binary_search(dummy_array, 8)
    print(target_index)
