
import os
import shutil

def backup_files(source_dir, backup_dir):
    # Ensure the backup directory exists
    os.makedirs(backup_dir, exist_ok=True)

    # Iterate over files in the source directory
    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)
        backup_file = os.path.join(backup_dir, filename)

        # Skip directories, we only want to copy files
        if os.path.isfile(source_file):
            try:
                shutil.copy2(source_file, backup_file)  # Copy file with metadata
                print(f"Copied: {source_file} to {backup_file}")
            except IOError as e:
                print(f"Error copying {source_file}: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")

def main():
    source_dir = input("Enter the source directory: ")
    backup_dir = input("Enter the backup directory: ")

    if not os.path.exists(source_dir):
        print("Source directory does not exist.")
        return

    backup_files(source_dir, backup_dir)
    print("Backup completed successfully.")

if __name__ == "__main__":
    main()
