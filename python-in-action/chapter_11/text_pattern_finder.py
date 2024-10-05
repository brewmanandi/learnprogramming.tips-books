
import re

def find_pattern_in_file(pattern, filename):
    try:
        with open(filename, "r") as file:
            for line_number, line in enumerate(file, 1):
                matches = re.findall(pattern, line)
                if matches:
                    print(f"Line {line_number}: {line.strip()}")
                    print(f"Matches: {matches}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

def main():
    filename = input("Enter the filename: ")
    pattern = input("Enter the regex pattern: ")
    
    print(f"\nSearching for pattern '{pattern}' in '{filename}':")
    find_pattern_in_file(pattern, filename)

if __name__ == "__main__":
    main()
