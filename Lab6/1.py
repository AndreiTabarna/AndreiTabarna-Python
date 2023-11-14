import os
import sys

def print_file_contents(directory_path, file_extension):
    try:
        for filename in os.listdir(directory_path):
            if filename.endswith(file_extension):
                file_path = os.path.join(directory_path, filename)
                with open(file_path, 'r') as file:
                    print(f"Contents of {filename}:\n{file.read()}\n")
    except FileNotFoundError:
        print("Error: Directory not found.")
    except PermissionError:
        print("Error: Permission issue.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <directory_path> <file_extension>")
    else:
        directory_path, file_extension = sys.argv[1], sys.argv[2]
        print_file_contents(directory_path, file_extension)

