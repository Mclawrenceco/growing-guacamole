# File Renaming Script

This Python script allows you to rename files in a specified directory with a given prefix and optional new file extension. It is designed to be flexible, allowing you to rename files in any folder without modifying the script each time.

## Features

- Rename all files in a specified directory.
- Add a prefix to each file name.
- Optionally change the file extension.
- Sorts files to rename them in a predictable order.
- Allows repeated renaming without restarting the script.

## Requirements

- Python 3.x

## Setup

1. **Clone the repository or download the script**:

    ```sh
    git clone https://github.com/Mclawrenceco/growing-guacamole.git 
    cd growing-guacamole
    ```

2. **Ensure you have Python installed**:

    Verify you have Python 3 installed by running:

    ```sh
    python --version
    ```

    If not installed, download and install Python 3 from [python.org](https://www.python.org/).

## Usage

1. **Run the script**:

    Navigate to the directory containing the script and run it:

    ```sh
    python rename_files.py
    ```

2. **Provide the required inputs**:

    - **Directory path**: Enter the path to the folder containing the files you want to rename.
    - **Prefix**: Enter the prefix you want to add to each file name.
    - **New suffix (optional)**: Enter the new file extension (e.g., 'txt', 'jpg', 'mp3'). Leave empty to keep the original extension.

    Example:

    ```sh
    Enter the path to your folder: /path/to/your/folder
    Enter the desired prefix: new_name
    Enter the new suffix (e.g., 'txt', 'jpg', 'mp3'), or press Enter to keep original suffix:
    ```

3. **Repeat as needed**:

    The script will prompt if you want to rename files in another folder. Type `yes` to continue or `no` to exit.

    ```sh
    Do you want to rename files in another folder? (yes/no): yes
    ```

## Example

Assuming you have a folder `/path/to/your/folder` with files `file1.txt`, `file2.txt`, `file3.txt` and you run the script with the following inputs:

- Directory path: `/path/to/your/folder`
- Prefix: `renamed`
- New suffix: `md`

The files will be renamed to `renamed_001.md`, `renamed_002.md`, `renamed_003.md`.

## License

This project is licensed under the MIT License.
