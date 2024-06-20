import os
def create_directory(directory_name):
    try:
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    except FileExistsError:
        print(f"Directory '{directory_name}' already exists.")
    except OSError as e:
        print(f"Error occurred: {e}")
def list_directory(directory):
    try:
        print(f"Listing contents of directory '{directory}':")
        for item in os.listdir(directory):
            print(item)
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")
    except OSError as e:
        print(f"Error occurred: {e}")
def search_py_files(directory):
    try:
        print(f"Searching for .py files in directory '{directory}':")
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(".py"):
                    print(os.path.join(root, file))
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")
    except OSError as e:
        print(f"Error occurred: {e}")
def remove_file(file_path):
    try:
        os.remove(file_path)
        print(f"File '{file_path}' removed successfully.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except OSError as e:
        print(f"Error occurred: {e}")

def main():
    directory_name = "test_directory"
    file_to_remove = "test_file.txt"
    search_directory = "."  
    create_directory(directory_name)
    list_directory(directory_name)
    search_py_files(search_directory)
    with open(file_to_remove, 'w') as f:
        f.write("This is a test file.")
    remove_file(file_to_remove)

if __name__ == "__main__":
    main()
