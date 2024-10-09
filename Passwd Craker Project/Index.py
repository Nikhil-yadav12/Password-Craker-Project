import hashlib

# Function to hash the password using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# Function to perform dictionary attack
def dictionary_attack(hash_to_crack, wordlist_file):
    try:
        with open(wordlist_file, 'r', encoding='ISO-8859-1') as wordlist:
            for password in wordlist:
                password = password.strip()
                hashed_password = hash_password(password)
                
                if hashed_password == hash_to_crack:
                    print(f"[+] Password found: {password}")
                    return password
                
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
    # Hash of the password we're trying to crack (e.g., hash of 'password123')
    target_hash = "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f"
    
    # Wordlist file path
    wordlist_file = "wordlist.txt"
    
    # Call dictionary attack function
    dictionary_attack(target_hash, wordlist_file)
