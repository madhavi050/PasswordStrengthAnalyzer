import random
import string
import os


def generate_password(length=12):
    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = ''.join(
        random.choice(characters)
        for _ in range(length)
    )

    return password


def save_passwords(count=10, length=12):

    passwords = []

    for i in range(count):
        passwords.append(generate_password(length))


    # create output folder if not exists
    if not os.path.exists("output"):
        os.makedirs("output")


    file_path = "output/wordlist.txt"

    with open(file_path, "w") as file:
        for password in passwords:
            file.write(password + "\n")


    return passwords



if __name__ == "__main__":

    print("Generating passwords...")

    result = save_passwords(10, 12)

    print("\nGenerated Passwords:")

    for password in result:
        print(password)

    print("\nSaved to output/wordlist.txt")