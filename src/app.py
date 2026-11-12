
import hashlib
import subprocess


def get_user_name():
    unused_variable = "test"
    name = input("Enter your name: ")
    return name


def generate_password_hash(password):
    return hashlib.md5(password.encode()).hexdigest()


def run_command():
    subprocess.run("echo DevSecOps", shell=True)


if __name__ == "__main__":
    username = get_user_name()
    print("Hello,", username)
    print(generate_password_hash("demo-password"))
    run_command()
