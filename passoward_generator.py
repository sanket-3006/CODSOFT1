import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    password_length = int(input("Enter the desired password length: "))
    
    if password_length <= 0:
        print("Password length should be greater than 0.")
    else:
        generated_password = generate_password(password_length)
        print(f"Generated Password: {generated_password}")
