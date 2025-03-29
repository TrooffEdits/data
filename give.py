import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python send_command.py <command>")
    sys.exit(1)

command = sys.argv[1]

# Try 0x0.st first
response = requests.post("https://0x0.st", files={"f": command.encode()})

if response.status_code == 200:
    url = response.text.strip()
    print(f"Command sent! {url}")

    # Save the URL for the laptop
    with open("last_command_url.txt", "w") as file:
        file.write(url)
else:
    print("Failed to send command, trying backup...")

    # Try clbin.com as a backup
    response = requests.post("https://clbin.com", data=command)

    if response.status_code == 200:
        url = response.text.strip()
        print(f"Command sent via backup! {url}")

        with open("last_command_url.txt", "w") as file:
            file.write(url)
    else:
        print("Both services failed. Try again later.")
