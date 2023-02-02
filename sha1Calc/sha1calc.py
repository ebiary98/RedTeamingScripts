import hashlib
import os
import sys

def extract_sha1(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        sha1 = hashlib.sha1(data).hexdigest()
    return sha1

def process_folder(folder_path):
    with open("sha1_checksums.txt", "w") as f:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                sha1 = extract_sha1(file_path)
                f.write(f"{filename}: {sha1}\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python sha1calc.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    process_folder(folder_path)
