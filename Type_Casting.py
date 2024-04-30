def main():
    # Convert string to integer
    str_num = input("Enter a number as string: ")
    num_int = int(str_num)
    print("Integer value:", num_int)
    print("Type of num_int:", type(num_int))

    # Convert integer to float
    int_num = 10
    num_float = float(int_num)
    print("Float value:", num_float)
    print("Type of num_float:", type(num_float))

    # Convert integer to string
    int_val = 42
    val_str = str(int_val)
    print("String value:", val_str)
    print("Type of val_str:", type(val_str))

    # Convert boolean to integer
    bool_val = True
    val_int = int(bool_val)
    print("Integer value of boolean True:", val_int)

    # Convert boolean to string
    bool_val = False
    val_str = str(bool_val)
    print("String value of boolean False:", val_str)

if __name__ == "__main__":
    main()
