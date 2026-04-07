from getpass import getpass

try:
    from password_mask.password_utills import (
        KEY_FILE,
        PASSWORD_FILE,
        encrypt_password,
        fake_str,
        load_key,
    )
except ModuleNotFoundError:
    from password_utills import KEY_FILE, PASSWORD_FILE, encrypt_password, fake_str, load_key


if __name__ == "__main__":
    password = getpass("Enter MySQL password to encrypt once: ")
    if not password:
        raise ValueError("Password cannot be empty.")

    load_key()
    encrypt_password(password)
    print(f"Password encrypted successfully: {fake_str(password)}")
    print(f"Encrypted password saved to: {PASSWORD_FILE}")
    print(f"Secret key saved to: {KEY_FILE}")
