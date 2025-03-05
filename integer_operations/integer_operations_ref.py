def get_integer_list():
    """
    Asks the user for a comma-separated list of integers and returns it as a list.
    Handles potential ValueError if input is not valid.
    """
    while True:
        try:
            input_str = input("Enter a comma-separated list of integers: ")
            numbers = [int(x.strip()) for x in input_str.split(',')]
            return numbers
        except ValueError:
            print("Invalid input. Please enter integers separated by commas.")

def sort_ascending(numbers):
    """
    Sorts a list of numbers in ascending order.
    """
    return sorted(numbers, reverse=True)

def calculate_sum_first_two(numbers):
    """
    Calculates the sum of the first two numbers in a list.
    """
    if len(numbers) < 2:
        return "List must have at least two numbers."
    return numbers[0] + numbers[1]

def calculate_product_third_fourth(numbers):
    """
    Calculates the product of the third and fourth numbers in a list.
    """
    if len(numbers) < 4:
        return "List must have at least four numbers."
    return numbers[2] * numbers[3]

def calculate_division_last(numbers):
    """
    Divides the product of the third and fourth numbers by the last number in a list.
    """
    if len(numbers) < 1:
        return "List must have at least one number."
    if numbers[-1] == 0:
        return "Cannot divide by zero."
    return (calculate_sum_first_two(numbers) + calculate_product_third_fourth(numbers)) / numbers[-1]

if __name__ == "__main__":
    numbers = get_integer_list()
    sorted_numbers = sort_ascending(numbers)

    print("Sorted numbers:", sorted_numbers)

    sum_result = calculate_sum_first_two(sorted_numbers)
    print("Sum of first two:", sum_result)

    product_result = calculate_product_third_fourth(sorted_numbers)
    print("Product of third and fourth:", product_result)

    division_result = calculate_division_last(sorted_numbers)
    print("Division by last: {:.2f}".format(division_result))