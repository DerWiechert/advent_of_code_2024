import importlib

if __name__ == "__main__":
    print("Welcome to Advent of Code 2024")
    day_input = input("Which level would you like to execute: ")
    try:
        day = int(day_input)
    except:
        raise Exception("Please give a number!")
    solution = importlib.import_module(f"day{day}.solution")
    print(solution.solution())
