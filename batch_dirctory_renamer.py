import os

def rename_files(directory, prefix, new_suffix=None):
    # List all files in the directory
    files = os.listdir(directory)
    
    # Sort the files to ensure they are renamed in a predictable order
    files.sort()
    
    # Iterate over the files and rename them
    for i, filename in enumerate(files):
        # Extract the original file extension
        original_extension = os.path.splitext(filename)[1]
        
        # Use the new suffix if provided, otherwise keep the original extension
        if new_suffix:
            new_extension = new_suffix if new_suffix.startswith('.') else f'.{new_suffix}'
        else:
            new_extension = original_extension
        
        # Create the new name
        new_name = f"{prefix}_{i+1:03}{new_extension}"
        
        # Construct the full old and new file paths
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_name)
        
        # Rename the file
        os.rename(old_file, new_file)
        print(f"Renamed: {old_file} to {new_file}")

if __name__ == "__main__":
    while True:
        # Get user inputs
        directory = input("Enter the path to your folder (or type 'exit' to quit): ")
        if directory.lower() == 'exit':
            break
        
        prefix = input("Enter the desired prefix: ")
        new_suffix = input("Enter the new suffix (e.g., 'txt', 'jpg', 'mp3'), or press Enter to keep original suffix: ")

        # If new_suffix is an empty string, set it to None
        new_suffix = new_suffix if new_suffix else None
        
        # Call the rename_files function with user inputs
        rename_files(directory, prefix, new_suffix)

        # Ask if the user wants to rename more files
        continue_choice = input("Do you want to rename files in another folder? (yes/no): ")
        if continue_choice.lower() != 'yes':
            break
