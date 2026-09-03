def check_even_odd(number):
    """
    Determines whether a given number is even or odd.
    Uses the modulus (%) operator, which works correctly
    for negative numbers in Python as well.
    """
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


def main():
    try:
        num = int(input("Enter a number: "))
        result = check_even_odd(num)
        print(f"{num} is {result}.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")


if __name__ == "__main__":
    # Example runs demonstrating both even and odd inputs
    print("=== Example Runs ===")
    for example in [8, 7, -4, -3, 0]:
        print(f"{example} is {check_even_odd(example)}.")

    print("\n=== Interactive Mode ===")
    main()
