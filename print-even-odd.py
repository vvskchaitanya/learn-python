def print_even_numbers_up_to(end):
    for number in range(1, end + 1):
        if number % 2 == 0:
            print(number)

def print_odd_numbers_up_to(end):
    for number in range(1, end + 1):
        if number % 2 != 0:
            print(number)

if __name__ == "__main__":
    choice = input("Do you want to print 'even' or 'odd' numbers? ").strip().lower()
    end = int(input("Enter the end of the range: "))
    
    if choice == "even":
        print_even_numbers_up_to(end)
    elif choice == "odd":
        print_odd_numbers_up_to(end)
    else:
        print("Invalid choice. Please enter 'even' or 'odd'.")