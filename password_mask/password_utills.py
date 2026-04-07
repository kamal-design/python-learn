from pathlib import Path

from cryptography.fernet import Fernet


BASE_DIR = Path(__file__).resolve().parent
KEY_FILE = BASE_DIR / "secret.key"
PASSWORD_FILE = BASE_DIR / "encrypted_password.bin"


class FakeStr:
    def __init__(self, value: str, visible_chars: int = 2, mask_char: str = "*"):
        if visible_chars < 0:
            raise ValueError("visible_chars must be 0 or greater.")

        if len(mask_char) != 1:
            raise ValueError("mask_char must be a single character.")

        self._value = value or ""
        self._visible_chars = visible_chars
        self._mask_char = mask_char

    def masked(self) -> str:
        if not self._value:
            return ""

        if len(self._value) <= self._visible_chars:
            return self._mask_char * len(self._value)

        masked_length = len(self._value) - self._visible_chars
        return f"{self._mask_char * masked_length}{self._value[-self._visible_chars:]}"

    def reveal(self) -> str:
        return self._value

    def __str__(self) -> str:
        return self.masked()

    def __repr__(self) -> str:
        return self.masked()

    def __format__(self, format_spec: str) -> str:
        return format(self.masked(), format_spec)


def fake_str(value: str, visible_chars: int = 2, mask_char: str = "*") -> FakeStr:
    return FakeStr(value, visible_chars=visible_chars, mask_char=mask_char)


def load_key() -> bytes:
    if KEY_FILE.exists() and KEY_FILE.stat().st_size > 0:
        return KEY_FILE.read_bytes()

    key = Fernet.generate_key()
    KEY_FILE.write_bytes(key)
    return key


def encrypt_password(plain_password: str) -> bytes:
    key = load_key()
    cipher = Fernet(key)
    encrypted_password = cipher.encrypt(plain_password.encode("utf-8"))
    PASSWORD_FILE.write_bytes(encrypted_password)
    return encrypted_password


def decrypt_password() -> str:
    if not KEY_FILE.exists() or KEY_FILE.stat().st_size == 0:
        raise FileNotFoundError(
            f"Missing Fernet key file: {KEY_FILE}. Run encrypt_once.py first."
        )

    if not PASSWORD_FILE.exists() or PASSWORD_FILE.stat().st_size == 0:
        raise FileNotFoundError(
            f"Missing encrypted password file: {PASSWORD_FILE}. Run encrypt_once.py first."
        )

    key = load_key()
    encrypted_password = PASSWORD_FILE.read_bytes()
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_password).decode("utf-8")
