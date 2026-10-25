#validate input
# keep asking for input until the user for inpuyt number between 1 and 10

while True:
    user_input = int(input("Enter a number between 1 and 10: "))
    if 1 <= user_input <= 10:
        print(f"You entered: {user_input}")
        break
    else:
        print("Invalid input. Please try again.")