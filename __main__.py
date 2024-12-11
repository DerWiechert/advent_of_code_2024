import importlib


def day_input():
    day_input = input("Which level would you like to execute: ")
    try:
        day = int(day_input)
    except:
        raise Exception("Please give a number!")
    return day


def part_input():
    part_input = input("Execute part 1 or 2: ")
    try:
        part = int(part_input)
    except:
        raise Exception("Please give a number!")
    return part


if __name__ == "__main__":
    print("Welcome to Advent of Code 2024")
    day = day_input()
    part = part_input()
    solution = importlib.import_module(f"day{day}.solution")
    print(eval(f"solution.solution{part}()"))
