## Step 1: Raw / Messy Code (Before Principles)

# Messy code – not modular, not reusable, hard to maintain
import random

numbers = [random.randint(1, 100) for _ in range(10)]
print("Generated numbers:", numbers)

# Calculate average
total = 0
for n in numbers:
    total += n
average = total / len(numbers)
print("Average:", average)

# Find max
max_num = numbers[0]
for n in numbers:
    if n > max_num:
        max_num = n
print("Max:", max_num)


"""
🔴 Problems:

No functions (not modular).

Can’t reuse logic elsewhere.

Hard to extend (e.g., adding min/median).

Not scalable (works only for small lists).

No error handling (reliability issue).

No comments/documentation.
"""

## Step 1: Refactored Code (With Principles)

import random
from typing import List

def generate_numbers(count: int, lower: int = 1, upper: int = 100) -> List[int]:
    """Generate a list of random integers."""
    return [random.randint(lower, upper) for _ in range(count)]

def calculate_average(numbers: List[int]) -> float:
    """Return the average of a list of numbers."""
    if not numbers:
        raise ValueError("List of numbers cannot be empty")
    return sum(numbers) / len(numbers)

def find_max(numbers: List[int]) -> int:
    """Return the maximum number from a list."""
    if not numbers:
        raise ValueError("List of numbers cannot be empty")
    return max(numbers)

if __name__ == "__main__":
    # Example workflow (can be reused in other projects)
    nums = generate_numbers(10)
    print("Generated numbers:", nums)
    print("Average:", calculate_average(nums))
    print("Max:", find_max(nums))

"""
✅ Improvements:

Modularity: Code broken into functions.

Reusability: Functions can be used in any project.

Maintainability: Easy to add min/median later.

Scalability: Can handle larger datasets (just change count).

Reliability & Quality: Error handling included.

Security & Trust: Checks against empty input.

Collaboration: Docstrings/comments make it understandable for teams.
"""

### Classroom Activity 

## Step 2: Refactored Pandas Code (With Principles)

import pandas as pd

IRIS_URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"


def load_data(source: str) -> pd.DataFrame:
    """Load a CSV file (local path or URL) into a DataFrame."""
    try:
        df = pd.read_csv(source)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {source}")
    except Exception as e:
        raise RuntimeError(f"Could not load data from {source}: {e}")

    if df.empty:
        raise ValueError("Loaded dataset is empty")
    return df


def check_column(df: pd.DataFrame, column: str) -> None:
    """Raise an error if the column does not exist in the DataFrame."""
    if column not in df.columns:
        raise KeyError(
            f"Column '{column}' not found. Available columns: {list(df.columns)}"
        )


def column_mean(df: pd.DataFrame, column: str) -> float:
    """Return the average value of a numeric column."""
    check_column(df, column)
    return df[column].mean()


def column_max(df: pd.DataFrame, column: str) -> float:
    """Return the maximum value of a numeric column."""
    check_column(df, column)
    return df[column].max()


def filter_rows(df: pd.DataFrame, column: str, value) -> pd.DataFrame:
    """Return only the rows where the column equals the given value."""
    check_column(df, column)
    return df[df[column] == value]


if __name__ == "__main__":
    # Example workflow (can be reused with any CSV and any column)
    iris = load_data(IRIS_URL)

    print("Average sepal length:", column_mean(iris, "sepal_length"))
    print("Max petal width:", column_max(iris, "petal_width"))

    setosa = filter_rows(iris, "species", "setosa")
    print(setosa.head())


"""
✅ Improvements:

Modularity: Loading, calculating, and filtering are separate functions.

Reusability: Functions take any DataFrame and column name, so they work
on other datasets, not just iris.

Maintainability: Adding a new stat (e.g., column_min or column_median)
is just one more small function.

Scalability: Easy to loop over multiple CSVs or columns using the same
functions.

Reliability & Quality: Errors are caught when the file can't load, the
data is empty, or a column name is wrong.

Security & Trust: check_column validates input before using it, and
gives a clear message listing the real column names.

Collaboration: Docstrings and a named constant (IRIS_URL) make the code
easy for teammates to read and change.
"""
