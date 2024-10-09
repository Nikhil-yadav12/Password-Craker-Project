import hashlib
import os

# Function to hash the password using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# Function to save the hashed password to a file
def save_password(password, filename):
    hashed_password = hash_password(password)
    with open(filename, 'a') as f:  # Append to the file
        f.write(hashed_password + '\n')
    print(f"[+] Password saved. Hashed value: {hashed_password}")

# Function to perform dictionary attack
def dictionary_attack(hash_to_crack, wordlist_file):
    try:
        with open(wordlist_file, 'r', encoding='ISO-8859-1') as wordlist:
            for password in wordlist:
                password = password.strip()
                
                # Calculate hash of the current password
                hashed_password = hash_password(password)
                
                if hashed_password == hash_to_crack:
                    print(f"[+] Password found: {password}")
                    return password  # Return the found password
                
        print("[-] Password not found in wordlist.")
        return None
    except FileNotFoundError:
        print(f"[-] Wordlist file {wordlist_file} not found.")
        return None
    except UnicodeDecodeError as e:
        print(f"[-] Encoding error: {e}")
        return None

# Main function
if __name__ == "__main__":
    option = input("Choose an option:\n1. Save a password\n2. Crack a password\n> ")

    if option == '1':
        password_to_save = input("Enter the password to save: ")
        save_password(password_to_save, 'saved_passwords.txt')  # Save to a file
    elif option == '2':
        # Get the hash from the saved passwords file
        if os.path.exists('saved_passwords.txt'):
            print("Saved passwords (hashed):")
            with open('saved_passwords.txt', 'r') as f:
                saved_hashes = f.readlines()
                for saved_hash in saved_hashes:
                    print(saved_hash.strip())
            hash_to_crack = input("Enter the hash to crack: ")
            wordlist_file = "wordlist.txt"
            dictionary_attack(hash_to_crack.strip(), wordlist_file)
        else:
            print("No saved passwords found. Please save a password first.")
    else:
        print("Invalid option. Please choose 1 or 2.")
2