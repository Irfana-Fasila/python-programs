def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source, open(destination_file, 'w') as destination:
            for line in source:
                destination.write(line)
        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
    except IOError:
        print("Error occurred while reading/writing the file.")

def main():
    source_file = input("Enter the path of the source file: ")
    destination_file = input("Enter the path of the destination file: ")
    
    copy_file(source_file, destination_file)

if __name__ == "__main__":
    main()
