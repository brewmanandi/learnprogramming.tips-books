
# File Backup Utility

## Overview

The **File Backup Utility** is a Python application that allows users to copy files from one directory to another (a backup directory). It handles both text and binary files and ensures that files are copied with their metadata intact.

## Features

- **Backup Files**: Copy all files from a source directory to a backup directory.
- **Handles Binary and Text Files**: Supports both types of files, including images, documents, and more.
- **Error Handling**: The app gracefully handles file I/O errors such as file not found or permission errors.

## How to Run the Program

### Requirements:
- Python 3.x

### Steps:
1. Download the `backup_utility.py` file from this repository.
2. Open a terminal or command prompt and navigate to the directory where `backup_utility.py` is saved.
3. Run the program using the following command:

    ```bash
    python backup_utility.py
    ```

4. Follow the prompts to enter the source directory and the backup directory. The utility will copy all files from the source to the backup location.

## Example Interaction

```text
Enter the source directory: /path/to/source
Enter the backup directory: /path/to/backup
Copied: /path/to/source/file1.txt to /path/to/backup/file1.txt
Copied: /path/to/source/image.jpg to /path/to/backup/image.jpg
Backup completed successfully.
```

## License

This project is open-source and available for educational purposes. Feel free to modify and share it!
