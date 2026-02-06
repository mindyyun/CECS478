# Emma Tu, Mindy Yun
# Contributions: Emma - 50%, Mindy - 50%

# Define a fixed maximum buffer size
MAX_BUFFER_SIZE = 10


def safe_input(user_input: str) -> str:
    """
    Safely stores user input by checking length before accepting it.
    This prevents overflow-style issues by rejecting oversized input.
    """

    # Defensive check: reject input that exceeds buffer size
    if len(user_input) > MAX_BUFFER_SIZE:
        raise ValueError(
            f"Input too long. Maximum allowed length is {MAX_BUFFER_SIZE} characters."
        )

    # If input is safe, return it
    return user_input


def main():
    try:
        # Ask user for input
        data = input(f"Enter a string (max {MAX_BUFFER_SIZE} characters): ")

        # Attempt to safely store the input
        safe_data = safe_input(data)

        print("Input accepted safely.")
        print("Stored data:", safe_data)

    except ValueError as error:
        # Handle invalid input safely instead of crashing
        print("Error:", error)


# Run the program
if __name__ == "__main__":
    main()