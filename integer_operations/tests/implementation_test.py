import random
from integer_operations_implementation import IntegerOperations

test_list = [random.randint(1,100) for _ in range(5)]

sorted_test_list = sorted(test_list, reverse=True)

test_object = IntegerOperations()

test_object.numbers = test_list

def test_sort():
    test_object.sort_numbers()
    assert test_object.numbers  == sorted_test_list

def test_sum():
    assert test_object.sum_of_first_and_second() == sorted_test_list[0] + sorted_test_list[1]

def test_product():
    assert test_object.product_of_third_and_fourth() == sorted_test_list[2] * sorted_test_list[3]

def test_quotient():
    assert test_object.quotient_of_fifth() == ((sorted_test_list[0]+sorted_test_list[1])+(sorted_test_list[2]*sorted_test_list[3])) / sorted_test_list[-1]