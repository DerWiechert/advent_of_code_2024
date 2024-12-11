from library.get_src import get_source


def get_lists(source):
    first_list = []
    second_list = []
    for pair in source.split("\n"):
        if not pair:
            continue
        first, second = pair.split("   ")
        first_list.append(first)
        second_list.append(second)
    return first_list, second_list


def get_distance(first_list, second_list):
    distance = 0
    for item1, item2 in zip(first_list, second_list):
        distance += abs(int(item1) - int(item2))
    return distance


def solution1():
    source = get_source(1)
    first_list, second_list = get_lists(source)
    first_list.sort()
    second_list.sort()
    return get_distance(first_list, second_list)


def solution2():
    source = get_source(1)
    first_list, second_list = get_lists(source)
    result = 0
    for item in first_list:
        result += int(item) * second_list.count(item)
    return result
