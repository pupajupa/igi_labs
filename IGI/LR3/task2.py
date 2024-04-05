import generator
import checking


def calculate_sum_of_squares(numbers):
    """
    Calculate the sum of squares of a list of numbers.

    Args:
    numbers (list): The list of numbers.

    Returns:
    int: The sum of squares.
    """
    return sum([x ** 2 for x in numbers])


def task2():
    """
    Prints the result of the sum of squared numbers.
    """
    choice = checking.check_input("Enter '1' for keyboard input or '2' for random number generation: ", 1, 2, int)
    total = 0

    if choice == 1:
        while True:
            number = checking.check_input("Enter an integer (0 to exit): ", -50, 50, int)
            total += number ** 2
            if number == 0:
                break
    else:
        seq = list(generator.generate_int_sequence(checking.check_input("Enter the number of list items: ", 1, 50, int)))
        print(seq)
        total = sum([x ** 2 for x in seq])

    print("The sum of the squared numbers is:", total)