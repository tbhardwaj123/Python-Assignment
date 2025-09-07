try:
    with open("sample.txt", "r") as file1:
        reading_file = file1.read()
        print("Reading file content:")
        print(reading_file)

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")


