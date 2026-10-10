# Three Stacks in a Single Array

A Data Structures and Algorithms assignment exploring how three stacks can share one fixed-size array in Python.

## Overview

The `ThreeColorStacks` class manages three stacks named Red, Blue, and Green:

- **Red:** Starts at the beginning of the array and grows right.
- **Blue:** Starts at the end of the array and grows left.
- **Green:** Starts near the middle and grows right. It can shift left or right to make room for other stacks.

The implementation explores stack operations, array indexing, and shared storage management.

## Features

- Push, pop, and peek operations for each stack.
- Methods for shifting the Green stack.
- Error handling for empty-stack operations.
- Overflow checks when attempting to add elements.
- A debugging method that displays the array and stack positions.

## Requirements

- Python 3
- No external libraries required.

## How to Run

Save the Python code as `three_color_stacks.py`, then run:

```bash
python3 three_color_stacks.py
```

The included demonstration creates an array with ten positions, pushes values onto each stack, and prints the internal state before and after removing elements.

## Example Usage

```python
from three_color_stacks import ThreeColorStacks

stacks = ThreeColorStacks(10)

stacks.push_red(1)
stacks.push_green(50)
stacks.push_blue(100)

print(stacks.peek_red())     # 1
print(stacks.peek_green())   # 50
print(stacks.peek_blue())    # 100

stacks.debug_print()
```

## Available Operations

| Stack | Add an element | Remove the top element | View the top element |
|---|---|---|---|
| Red | `push_red(x)` | `pop_red()` | `peek_red()` |
| Blue | `push_blue(x)` | `pop_blue()` | `peek_blue()` |
| Green | `push_green(x)` | `pop_green()` | `peek_green()` |

`debug_print()` displays the backing array and stack indices.

## Complexity

- **Peek and pop:** O(1).
- **Push without shifting:** O(1).
- **Push requiring a Green-stack shift:** O(g), where g is the number of Green-stack elements.
- **Array storage:** O(N), where N is the array capacity.

## Known Limitations

This is an educational implementation and has not been fully tested for all boundary cases.

The collision check in `push_red()` uses `>` instead of detecting equality at the Green stack's starting position. Consequently, a Red-stack insertion can overwrite a Green-stack element. Boundary handling, including shifting an empty Green stack, requires further review.

## Author

Muhammad Taaha Mahmood
