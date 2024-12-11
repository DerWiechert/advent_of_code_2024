from library.get_src import get_source


def is_sorted(item_list, reverse=False):
    list_copy = item_list.copy()
    list_copy.sort(reverse=reverse)
    return item_list == list_copy


def check_sorted(item_list, remove):
    def condition(item_list):
        unique_list = []
        for val in item_list:
            if val in unique_list:
                return False
            unique_list.append(val)
        return is_sorted(item_list) or is_sorted(item_list, reverse=True)

    if condition(item_list):
        return item_list
    elif not remove:
        return False
    for idx in range(len(item_list)):
        tmp_list = [x for i, x in enumerate(item_list) if i != idx]
        if condition(tmp_list):
            return tmp_list
    return False


def get_list(line):
    tmp_list = line.split(" ")
    return [int(x) for x in tmp_list]


def check_adjacent_level(item_list):
    for idx in range(1, len(item_list)):
        diff = abs(item_list[idx] - item_list[idx - 1])
        if diff < 1 or diff > 3:
            return False
    return True


def get_increasing_decreasing_lists(source, remove=False):
    increasing_decreasing_lists = []
    for line in source.split("\n"):
        item_list = get_list(line)
        item_list = check_sorted(item_list, remove=remove)
        if item_list:
            increasing_decreasing_lists.append(item_list)
    return increasing_decreasing_lists


def solution1():
    source = get_source(2)
    increasing_decreasing_lists = get_increasing_decreasing_lists(source)
    result = 0
    for item_list in increasing_decreasing_lists:
        if check_adjacent_level(item_list):
            result += 1
    return result


def solution2():
    # WIP: Doesnt work
    source = get_source(2)
    increasing_decreasing_lists = get_increasing_decreasing_lists(source, remove=True)
    result = 0
    for item_list in increasing_decreasing_lists:
        if check_adjacent_level(item_list):
            result += 1
    return result
