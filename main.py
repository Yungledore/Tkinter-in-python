import random
import string

def generate_password(length):
    character_pool = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

if __name__ == "__main__":
    try:
        user_length = int(input("enter the desired password length:"))
        if user_length < 1:
            print("Please enter a length greater than 0.")
        else:
            new_password = generate_password(user_length)
            print(f"your new random password is: {new_password}")
    except ValueError:
        print("invalid input Please enter a number for the password length")