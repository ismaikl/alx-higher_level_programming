#!/usr/bin/python3
import sys

def main():
    # Initialize the sum to 0
    total = 0

    # Iterate over the arguments (excluding the script name)
    for arg in sys.argv[1:]:
        # Convert the argument to an integer and add it to the total
        total += int(arg)

    # Print the total
    print(total)

# Ensure the script doesn't run when imported
if __name__ == "__main__":
    main()
