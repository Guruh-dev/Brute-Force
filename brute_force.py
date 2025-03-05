import time
import argparse

def load_passwords(file_path):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []

def load_targets(file_path):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []

def brute_force(target_password, password_list, delay=0.1):
    for password in password_list:
        if password == target_password:
            return password
        time.sleep(delay)
    return None

def main():
    parser = argparse.ArgumentParser(description="Brute Force Password Cracker")
    parser.add_argument("password_list", help="The file containing the list of passwords")
    parser.add_argument("targets", help="The file containing the list of target passwords")
    parser.add_argument("--delay", type=float, default=0.1, help="Delay between attempts (default: 0.1 seconds)")

    args = parser.parse_args()

    password_list = load_passwords(args.password_list)
    targets = load_targets(args.targets)

    if not password_list or not targets:
        return

    for target in targets:
        found_password = brute_force(target, password_list, args.delay)
        if found_password:
            print(f"Password found for target '{target}': {found_password}")
        else:
            print(f"Password not found for target '{target}'")

if __name__ == "__main__":
    main()