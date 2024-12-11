def get_source(day):
    file = open(f"day{day}/src.txt", "r")
    return file.read()


def wip(func):
    print("This solution is still work in progress")
    return func
