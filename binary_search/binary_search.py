import time

def get_halfway_index(length):
    print(length)
    return int(round((length / 2), 0))

def binary_search(numbers, search):
    numbers.sort()
    halfway_index = get_halfway_index(len(numbers))
    print(halfway_index)
    halfway = numbers[halfway_index]
    print("Halfway number is %s" % halfway)
    if halfway == search:
        print("Found the search item")
        return halfway_index
    elif halfway > search:
        new_numbers_list_to_search = numbers[:halfway_index]
        print("New numbers list to search: ")
        print(new_numbers_list_to_search)
        binary_search(new_numbers_list_to_search, search)
        time.sleep(5)
    else:
        new_numbers_list_to_search = numbers[halfway_index:]
        print("New numbers list to search: ")
        print(new_numbers_list_to_search)
        binary_search(new_numbers_list_to_search, search)
        time.sleep(5)
