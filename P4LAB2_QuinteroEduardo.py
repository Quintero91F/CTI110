#EduardoQuintero Paz
#04/21/2025
#Making a times table program
def display_multiplication_table(n):
    print(f"\nMultiplication Table for {n}:")
    for i in range(1, 13):
        print(f"{n} x {i} = {n * i}")

def main():
    while True:
        try:
            user_input = int(input("Enter a non-negative integer: "))
            
            if user_input < 0:
                print("You cannot enter negative values.")
            else:
                display_multiplication_table(user_input)
        
        except ValueError:
            print("Invalid input. Please enter an integer.")
        
        # Ask if the user wants to run the program again
        again = input("Do you want to run the program again? (yes/no): ").strip().lower()
        if again != "yes":
            break

# Run the program
if __name__ == "__main__":
    main()
