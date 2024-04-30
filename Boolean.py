def get_boolean_input(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ["true", "t", "yes", "y", "1"]:
            return True
        elif response in ["false", "f", "no", "n", "0"]:
            return False
        else:
            print("Invalid input. Please enter 'true' or 'false'.")

def main():

    is_valid = get_boolean_input("Enter a boolean value (true/false): ")

    print("You entered:", is_valid)

if __name__ == "__main__":
    main()
