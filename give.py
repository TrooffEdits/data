import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python send_command.py <command>")
    sys.exit(1)

command = sys.argv[1]

# Send the command
response = requests.post("http://ix.io", data={"f:1": command})

if response.status_code == 200:
    url = response.text.strip()
    print(f"Command sent! {url}")

    # Save the URL for the laptop
    with open("last_command_url.txt", "w") as file:
        file.write(url)
else:
    print("Failed to send command.")
