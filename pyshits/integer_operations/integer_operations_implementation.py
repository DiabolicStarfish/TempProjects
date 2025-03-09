class IntegerOperations:

    def __init__(self):
        self.numbers = []

    def sort_numbers(self):
        self.numbers = sorted(self.numbers, reverse=True)

    def get_integer_list(self):
        try:
            input_str = input("Enter a comma-separated list of integers: ")
            self.numbers = [int(x.strip()) for x in input_str.split(',')]
        except ValueError:
            print("Invalid input.")

    def sum_of_first_and_second(self):
        return self.numbers[0] + self.numbers[1]
    
    def product_of_third_and_fourth(self):
        return self.numbers[2] * self.numbers[3]            
    
    def quotient_of_fifth(self):
        return (self.sum_of_first_and_second() + self.product_of_third_and_fourth()) / self.numbers[-1]
    
    def process_display(self):
        self.get_integer_list()
        self.sort_numbers()
        print("Sorted integer list: ", self.numbers)
        print("Sum of first and second number: ", self.sum_of_first_and_second())
        print("Product of third and fourth number: ", self.product_of_third_and_fourth())
        print("Quotient of fifth number: {:.2f}".format(self.quotient_of_fifth()))