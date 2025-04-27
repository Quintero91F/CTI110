# Eduardo Quintero Paz
# 04/21/2025
# Making a times table program WITHOUT functions

while True:
    try:
        user_input = int(input("Enter a non-negative integer: "))
        
        if user_input < 0:
            print("You cannot enter negative values.")
        else:
            print(f"\nMultiplication Table for {user_input}:")
            for i in range(1, 13):
                print(f"{user_input} x {i} = {user_input * i}")
    
    except ValueError:
        print("Invalid input. Please enter an integer.")
    
    # Ask if the user wants to run the program again
    again = input("Do you want to run the program again? (yes/no): ").strip().lower()
    if again != "yes":
        break
