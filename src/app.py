
import hashlib
import sys


def calculate_hash(message):
    """Generate a secure SHA-256 hash."""
    return hashlib.sha256(message.encode("utf-8")).hexdigest()


def show_python_version():
    """Display Python version without using subprocess."""
    return sys.version.split()[0]


if __name__ == "__main__":
    print("DevSecOps Security Demo")
    print("SHA-256:", calculate_hash("hello"))
    print("Python version:", show_python_version())

