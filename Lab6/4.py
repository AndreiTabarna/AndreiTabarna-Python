import os
import sys

def count_files_by_extension(directory_path):
    try:
        files = os.listdir(directory_path)
        extension_counts = {}
        for filename in files:
            _, extension = os.path.splitext(filename)
            if extension:
                extension = extension[1:]
                extension_counts[extension] = extension_counts.get(extension, 0) + 1
        for extension, count in extension_counts.items():
            print(f"Files with extension .{extension}: {count}")
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
        count_files_by_extension(directory_path)

