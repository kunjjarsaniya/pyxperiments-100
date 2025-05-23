# -----------------------------------------------
# Fibonacci Sequence Generator in Python
# -----------------------------------------------

# Description: This program generates the Fibonacci sequence up to a specified number of terms.

def generate_fibonacci(n_terms):
    """
    Generate a list containing the Fibonacci sequence up to n_terms.
    
    Parameters:
    n_terms (int): Number of terms in the Fibonacci sequence to generate
    
    Returns:
    list: A list containing the Fibonacci sequence
    """

    # Handle the case when the number of terms is less than or equal to 0
    if n_terms <= 0:
        return []

    # If only 1 term is requested, return [0]
    elif n_terms == 1:
        return [0]

    # If 2 terms are requested, return [0, 1]
    elif n_terms == 2:
        return [0, 1]

    # Start the sequence with the first two Fibonacci numbers
    fib_sequence = [0, 1]

    # Loop to generate the remaining terms
    for i in range(2, n_terms):
        next_term = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_term)  # Add the next term to the list

    return fib_sequence


# === Program Entry Point ===
if __name__ == "__main__":
    print("=== Fibonacci Sequence Generator ===")
    
    try:
        # Ask the user how many terms they want to generate
        num = int(input("Enter the number of terms you want: "))
        
        # Generate and display the sequence
        result = generate_fibonacci(num)
        print(f"\nFibonacci sequence with {num} terms:")
        print(result)

    except ValueError:
        # Handle non-integer inputs gracefully
        print("Please enter a valid integer.")
        
