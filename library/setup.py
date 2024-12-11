import os

PYTHON_SOLUTION_TEMPLATE = """\
from library.src import get_source, wip


@wip
def solution1():
    source = get_source(%(day)s)


@wip
def solution2():
    source = get_source(%(day)s)
"""


def setup_day():
    day = input("Which day to setup: ")
    path = os.getcwd() + f"/day{day}"
    if os.path.isdir(path):
        print("folder already exists!")
        return
    os.mkdir(path)
    open(path + "/__init__.py", "a").close()
    open(path + "/src.txt", "a").close()
    solution_py = open(path + "/solution.py", "a")
    solution_py.write(PYTHON_SOLUTION_TEMPLATE.format(day=day))


setup_day()
