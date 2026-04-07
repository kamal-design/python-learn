# pip install pymysql cryptography
from getpass import getpass
from pathlib import Path

import pymysql
from cryptography.fernet import InvalidToken

try:
    from password_mask.password_utills import (
        decrypt_password,
        encrypt_password,
        KEY_FILE,
        PASSWORD_FILE,
        load_key,
    )
except ModuleNotFoundError:
    from password_utills import (
        decrypt_password,
        encrypt_password,
        KEY_FILE,
        PASSWORD_FILE,
        load_key,
    )


def reset_saved_password_file() -> None:
    password_file = Path(PASSWORD_FILE)
    if password_file.exists():
        password_file.unlink()


def is_local_host(host: str) -> bool:
    return host in {"localhost", "127.0.0.1"}


def get_or_create_password(host: str) -> str:
    try:
        return decrypt_password()
    except (FileNotFoundError, InvalidToken):
        load_key()
        reset_saved_password_file()

        if is_local_host(host):
            print("Using empty password for localhost.")
            return ""

        plain_password = getpass("Enter MySQL password for first-time setup: ")
        if not plain_password:
            raise ValueError("Password cannot be empty for live/server connection.")

        encrypt_password(plain_password)
        print(f"Password saved securely: {plain_password}")
        return plain_password


def get_mysql_connection(
    host: str = "localhost",
    user: str = "root",
    database: str = "python_db", # Change to your database name if needed
    port: int = 3306,
):
    password = get_or_create_password(host)
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=port,
        cursorclass=pymysql.cursors.DictCursor,
    )
    print(f"Connected successfully to database: {database}")
    return connection


if __name__ == "__main__":
    connection = None
    try:
        connection = get_mysql_connection()
    except Exception as error:
        print(f"Connection failed: {error}")
    finally:
        if connection is not None:
            connection.close()
            print("Connection closed")
