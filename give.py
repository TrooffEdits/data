import requests
import sys

UPLOAD_URL = "https://ttm.sh"  # You can also use "https://transfer.sh"

if len(sys.argv) != 2:
    print("Usage: python send_command.py <command>")
    sys.exit(1)

command = sys.argv[1].encode()
response = requests.post(UPLOAD_URL, files={"file": command})

if response.status_code == 200:
    url = response.text.strip()
    print(f"Command stored: {url}")

    with open("last_command_url.txt", "w") as file:
        file.write(url)
else:
    print("Failed to send command.")
