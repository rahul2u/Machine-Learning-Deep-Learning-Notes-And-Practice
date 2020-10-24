def add_numbers(number1, number2):
    return number1 + number2


def main():
    first_number = int(input("Enter the first Number:"))
    second_number = int(input("Enter the second Number:"))
    sum_of_numbers = add_numbers(first_number, second_number)
    print("Sum of two number is :", sum_of_numbers)


if __name__ == '__main__':
    main()
