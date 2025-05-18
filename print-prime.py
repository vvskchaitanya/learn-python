def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes_up_to(end):
    for number in range(1, end + 1):
        if is_prime(number):
            print(number)

if __name__ == "__main__":
    end = int(input("Enter the end of the range: "))
    print_primes_up_to(end)