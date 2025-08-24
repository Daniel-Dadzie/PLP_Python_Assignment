# file_handling.py

def read_and_modify_file(filename):
    
    try:
        # Try to open the file in read mode
        with open('test.txt', "r") as file:
            content = file.read()
        
        # Modify the content (example: make all text uppercase)
        modified_content = content.upper()
        
        # Write modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)
        
        print(f"File read successfully! Modified content has been saved to '{new_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: Could not read or write to the file '{filename}'.")

def main():
    """
    Main function: asks user for filename and processes it.
    """
    filename = input("Enter the filename you want to read: ")
    read_and_modify_file(filename)

if __name__ == "__main__":
    main()
