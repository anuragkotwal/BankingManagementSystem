from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as file:
        file.write(key)
def load_key():
    return open("secret.key", "rb").read()

