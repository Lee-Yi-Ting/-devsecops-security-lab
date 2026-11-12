
import hashlib
import subprocess


def calculate_hash(message):
    """Generate a secure SHA-256 hash."""
    return hashlib.sha256(message.encode("utf-8")).hexdigest()


def run_command():
    """Execute a command without invoking a shell."""
    result = subprocess.run(
        ["python", "--version"],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout or result.stderr


if __name__ == "__main__":
    print("DevSecOps Security Demo")
    print("SHA-256:", calculate_hash("hello"))
    print(run_command())
