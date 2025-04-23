import os
import requests
import subprocess

ACCESS_FILE = "access.txt"
DOWNLOAD_LINK = "https://raw.githubusercontent.com/mdmuradhasanmedia/FACEBOOK-CLONE/refs/heads/main/fbtool.py"  # Replace with the actual download link
DOWNLOADED_FILENAME = "fbtool.py"

def check_access(username, access_file=ACCESS_FILE):
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

def download_and_run(download_link, output_filename):
    """Downloads a file from the given link and attempts to run it as a Python script."""
    try:
        print(f"Downloading script from: {download_link}...")
        response = requests.get(download_link, stream=True)
        response.raise_for_status()  # Raise an exception for bad status codes

        with open(output_filename, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Successfully downloaded script as '{output_filename}'.")

        print(f"Attempting to run '{output_filename}'...")
        subprocess.run(["python", output_filename], check=True)
        print(f"'{output_filename}' execution finished.")

    except requests.exceptions.RequestException as e:
        print(f"Error during download: {e}")
        return False
    except subprocess.CalledProcessError as e:
        print(f"Error running '{output_filename}': {e}")
        return False
    except FileNotFoundError:
        print("Error: Python interpreter not found.")
        return False
    return True

def main():
    username = input("Enter your username to access the script: ")

    if check_access(username):
        print("Access granted.")
        download_and_run(DOWNLOAD_LINK, DOWNLOADED_FILENAME)
    else:
        print("Access denied. Username not found in the access list.")

if __name__ == "__main__":
    main()
