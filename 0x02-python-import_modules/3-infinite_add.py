#!/usr/bin/python3
import sys

def main():
    # Initialize sum to 0
    total = 0

    # Iterate over each argument (excluding the script name itself)
    for arg in sys.argv[1:]:
        # Convert each argument to an integer and add to total
        total += int(arg)

    # Print the total sum
    print(total)

if __name__ == "__main__":
    main()
