def check_access(username, access_file="access.txt"):
    """Checks if the given username exists in the access file."""
    try:
        with open(access_file, "r") as f:
            for line in f:
                if line.strip() == username:
                    return True
    except FileNotFoundError:
        print(f"Error: The file '{access_file}' was not found.")
        return False
    return False

def main():
    username = input("Enter your username to access the script: ")

    if check_access(username):
        print("Access granted. Running the script...")
        # Your main script logic goes here
        print("Script execution finished.")
    else:
        print("Access denied. Username not found in the access list.")

if __name__ == "__main__":
    main()
