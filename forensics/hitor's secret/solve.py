import zipfile

# Read passwords from passwords.txt into a list
with open('passwords.txt', 'r') as file:
    passwords = file.read().splitlines()

# Function to extract content from zip files using brute force
def brute_force_extract(zip_filename):
    with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
        for password in passwords:
            try:
                zip_ref.extractall(pwd=password.encode())
                for info in zip_ref.infolist():
                    with open(info.filename, 'r') as f:
                        content = f.read()
                print(f'Content of {zip_filename}: {content}')
                return True
            except:
                continue
    print(f'Failed to extract {zip_filename}')
    return False

# Iterate through the zip files
for i in range(1, 1001):
    zip_filename = f'file_{i}.zip'
    brute_force_extract(zip_filename)
