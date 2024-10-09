
# Password Cracker Project

## Overview

This project is a simple password cracker implemented in Python. It uses SHA-256 hashing to save and verify passwords and supports a dictionary attack method to crack hashed passwords using a wordlist.

## Features

- **Save Passwords**: Hashes a given password and saves it to a file.
- **Crack Passwords**: Attempts to find the plaintext password by comparing the hashed password against a list of potential passwords (wordlist).

## Requirements

- Python 3.x
- Basic understanding of hashing and password security

## Installation

1. Clone or download this repository to your local machine.
2. Make sure you have Python 3.x installed on your system.
3. Create a wordlist file named `wordlist.txt` in the project directory, containing potential passwords (one per line).

### Sample Wordlist

```
123456
password
qwerty
password123
```

## Usage

1. Open a terminal or command prompt.
2. Navigate to the project directory where the script is located.
3. Run the script using Python:

   ```bash
   python Index.py
   ```

4. Choose one of the following options:
   - **1**: Save a password
     - You will be prompted to enter the password you want to save. The hashed version will be saved to a file called `saved_passwords.txt`.
   - **2**: Crack a password
     - You will see the list of saved hashed passwords. Enter the hash you want to crack. The script will use the provided wordlist to find the matching plaintext password.

## Example Output

### Saving a Password

```
Choose an option:
1. Save a password
2. Crack a password
> 1
Enter the password to save: mysecretpassword
[+] Password saved. Hashed value: <hashed value>
```

### Cracking a Password

```
Choose an option:
1. Save a password
2. Crack a password
> 2
Saved passwords (hashed):
<hashed value>
Enter the hash to crack: <hashed value>
[+] Password found: mysecretpassword
```

### If No Password is Found

```
[-] Password not found in wordlist.
```

## Notes

- Make sure the `wordlist.txt` file is in the same directory as the script.
- The script currently saves hashed passwords in a file called `saved_passwords.txt`, which accumulates hashes each time you save a password.
- This project is for educational purposes only. Use it responsibly and ethically.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
