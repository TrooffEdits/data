import requests
import sys

UPLOAD_URL = "https://transfer.sh/file"

if len(sys.argv) != 2:
    print("Usage: python send_command.py <command>")
    sys.exit(1)

command = sys.argv[1].encode()
response = requests.put(UPLOAD_URL, data=command)

if response.status_code == 200:
    paste_url = response.text.strip()
    print(f"Command stored: {paste_url}")

    with open("last_command_url.txt", "w") as file:
        file.write(paste_url)
else:
    print("Failed to send command.")
    print("Response:", response.text)
