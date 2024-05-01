def main():
    # Define a sample string
    sample_string = "Hello, World!"

    # Length of the string
    print("Length of the string:", len(sample_string))

    # Convert string to uppercase
    print("Uppercase:", sample_string.upper())

    # Convert string to lowercase
    print("Lowercase:", sample_string.lower())

    # Count occurrences of a substring
    substring = "l"
    print("Occurrences of '{}' in the string:".format(substring), sample_string.count(substring))

    # Check if string starts with a substring
    prefix = "Hello"
    print("Starts with '{}':".format(prefix), sample_string.startswith(prefix))

    # Check if string ends with a substring
    suffix = "World!"
    print("Ends with '{}':".format(suffix), sample_string.endswith(suffix))

    # Find the index of a substring
    substring = "World"
    print("Index of '{}':".format(substring), sample_string.find(substring))

    # Replace a substring
    old_substring = "World"
    new_substring = "Python"
    replaced_string = sample_string.replace(old_substring, new_substring)
    print("After replacement:", replaced_string)

    # Split the string into a list of substrings
    split_string = "apple,banana,orange"
    substrings = split_string.split(",")
    print("Split string:", substrings)

if __name__ == "__main__":
    main()
