import os
import sys

def rename_files_with_prefix(directory_path):
    try:
        files = os.listdir(directory_path)
        for i, filename in enumerate(files):
            new_name = f"file{i + 1}.{filename.split('.')[-1]}"
            os.rename(os.path.join(directory_path, filename), os.path.join(directory_path, new_name))
            print(f"Renamed {filename} to {new_name}")
    except FileNotFoundError:
        print("Error: Directory not found.")
    except PermissionError:
        print("Error: Permission issue.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
    else:
        directory_path = sys.argv[1]
        rename_files_with_prefix(directory_path)

