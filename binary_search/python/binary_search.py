import copy


NUMBERS = [93,2,8,87,15,17,45,1,23,78,38,29,99,3,55,64,28,83,74,39,44,27,91,
           52,67,16,65,82,4,9,93,87,18]


def get_halfway_index(length):
    print(length)
    return int(round((length / 2), 0))


def binary_search(numbers, search, numbers_original = []):

    def print_numbers_list(numbers):
        print("New numbers list to search: ")
        print(numbers)
        print("\n")

    if not numbers_original:
        numbers_original = copy.copy(numbers)
        numbers = copy.deepcopy(numbers)
        numbers.sort()

    if len(numbers) == 0:
        print("Item not found")
        return -1

    halfway_index = get_halfway_index(len(numbers))
    halfway = numbers[halfway_index]
    print("Halfway number is %s" % halfway)

    if len(numbers) == 1:
        if halfway == search:
            print("Found the search item at...")
            index = numbers_original.index(search)
            print(index)
            return index
        else:
            print("Item not found")
            return -1

    if halfway == search:
        print("Found the search item at...")
        index = numbers_original.index(search)
        print(index)
        return index
    elif halfway > search:
        new_numbers_list_to_search = numbers[:halfway_index]
        print_numbers_list(new_numbers_list_to_search)
        return binary_search(new_numbers_list_to_search, search, numbers_original)
    else:
        new_numbers_list_to_search = numbers[(halfway_index + 1):]
        print_numbers_list(new_numbers_list_to_search)
        return binary_search(new_numbers_list_to_search, search, numbers_original)


assert binary_search(NUMBERS, 2) == 1

assert binary_search(NUMBERS, 8) == 2

assert binary_search(NUMBERS, 87) == 3

assert binary_search(NUMBERS, 999) == -1
