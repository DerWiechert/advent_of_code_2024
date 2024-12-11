# Advent of Code 2024

Welcome to my repository for **Advent of Code 2024**! 🎄✨ This project contains my solutions for the daily programming challenges provided by Eric Wastl during Advent.

## 🔧 Usage
Since input files cannot be shared due to copyright restrictions, users need to provide their own input files. Each challenge has its own subfolder (e.g., `day1`, `day2`, `day3`, ...). Place your input file as `src.txt` in the corresponding folder so the solutions can run correctly.

### Steps to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/DerWiechert/advent_of_code_2024.git
   cd advent_of_code_2024
   ```
2. Add your input file as `src.txt` in the respective `dayX` folder.
3. Run the program:
   ```bash
   python __main__.py
   ```
4. Enter the day and than the part you want to execute in the terminal

## 🎨 Repository Structure
The repository is divided as follows:

- **`__main__.py`**: The main script located in the root directory. It dynamically executes the solution script (`solution.py`) from the specified `dayX` folder.
- **`dayX/`**: Contains the solution for day `X`.
  - `__init__.py`: Marks the folder as a Python package.
  - `solution.py`: The Python script containing the solution for the day's challenge.
  - `src.txt`: The input file (to be provided by you).

## 📚 Requirements
This project is implemented in Python. Ensure that Python 3.8+ is installed.

No additional dependencies are required as only built-in functions are used.

## 🙏 Acknowledgments
A huge thank you to **Eric Wastl**, the creator of Advent of Code. This challenge is inspiring and a lot of fun every year! Check out the website and support Eric: [Advent of Code](https://adventofcode.com).

## 🔒 Note
Please respect the rules and do not share input files publicly. Doing so would violate Eric Wastl's copyright.

## 🚀 Best of Luck and Happy Coding!
I hope this repository helps you tackle the challenges. Enjoy solving the problems!
