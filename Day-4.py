# -----------------------------------------------
# Prime Number Finder
# -----------------------------------------------

# This script finds all prime numbers up to a number entered by the user.

def is_prime(number):
    """
    Function to check if a number is prime.
    A prime number is only divisible by 1 and itself.
    """
    if number <= 1:
        return False  # Numbers less than or equal to 1 are not prime

    # Check divisibility from 2 to the square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False  # Found a factor, not prime

    return True  # No factors found, number is prime


def find_primes_up_to(limit):
    """
    Finds all prime numbers from 2 up to a given limit.
    Returns a list of prime numbers.
    """
    primes = []  # List to store prime numbers

    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)

    return primes


def main():
    """
    Main function to handle user input and display results.
    """
    print("🔍 Prime Number Finder")
    print("----------------------")

    try:
        # Take input from user and convert to integer
        user_input = int(input("Enter a number to find all primes up to: "))

        if user_input < 2:
            print("⚠️ Please enter a number greater than or equal to 2.")
            return

        prime_numbers = find_primes_up_to(user_input)

        # Display the result
        print(f"\n✅ Prime numbers up to {user_input} are:")
        print(prime_numbers)

    except ValueError:
        print("❌ Invalid input! Please enter a valid number.")


# Run the main function
if __name__ == "__main__":
    main()
