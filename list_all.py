import os
import argparse

def list_files_and_directories(path):
    try:
        # Check if the provided path is a valid directory
        if os.path.isdir(path):
            # Iterate over the items in the directory
            for item_name in os.listdir(path):
                # Create the full path by joining the directory path and item name
                full_path = os.path.join(path, item_name)

                # Check if it's a file
                if os.path.isfile(full_path):
                    print(f"File: {full_path}")

                # Check if it's a directory
                elif os.path.isdir(full_path):
                    print(f"Directory: {full_path}")

        else:
            print(f"The provided path '{path}' is not a valid directory.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(description="List all files and directories in a directory.")
    parser.add_argument("path", help="The path to the directory.")
    
    # Parse the command-line arguments
    args = parser.parse_args()
    
    # Call the function with the provided path
    list_files_and_directories(args.path)
