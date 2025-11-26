# Напишіть програму, яка виконує переміщення дисків з стрижня А на стрижень С,
# використовуючи стрижень В як допоміжний.
# Диски мають різний розмір і розміщені на початковому стрижні
# у порядку зменшення розміру зверху вниз.
# Правила:
# 1. За один крок можна перемістити тільки один диск.
# 2. Диск можна класти тільки на більший диск або на порожній стрижень.
# Вхідними даними програми має бути число n — кількість дисків на початковому стрижні. Вихідними даними — логування послідовності кроків для переміщення дисків зі стрижня А на стрижень С.

import argparse

# Global state to track rod positions
rods = {"A": [], "B": [], "C": []}
MOVES_COUNT = 0


def display_rods():
    """Display the current state of all rods."""

    for rod_name in ["A", "B", "C"]:
        disks = rods[rod_name]
        print(f"Rod {rod_name}: {disks}")
    print("-" * 24)


def towers_of_hanoi(n, source="A", target="C", auxiliary="B"):
    """Solve the Towers of Hanoi problem and print the steps."""

    if n == 1:
        move_disk(source, target)
        return

    towers_of_hanoi(n - 1, source, auxiliary, target)
    move_disk(source, target)
    towers_of_hanoi(n - 1, auxiliary, target, source)


def move_disk(source, target):
    """Move the top disk from source rod to target rod."""
    global MOVES_COUNT
    MOVES_COUNT += 1

    disk = rods[source].pop()
    rods[target].append(disk)

    print(f"Move disk {disk} from {source} to {target}")
    display_rods()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Solve the Towers of Hanoi.")
    parser.add_argument(
        "n", type=int, default=3, nargs="?", help="Number of disks (positive integer)."
    )
    args = parser.parse_args()

    if args.n <= 0:
        print("Number of disks must be a positive integer.")
    else:

        # Initialize rods with disks on rod A (largest at bottom, smallest at top)
        rods = {"A": list(range(args.n, 0, -1)), "B": [], "C": []}

        print(f"Initial state with {args.n} disks:")
        display_rods()

        towers_of_hanoi(args.n)

        print(f"Final state after {MOVES_COUNT} moves:")
        display_rods()

# Example usage:
# python towers_of_hanoi.py 3
