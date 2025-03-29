import requests
import sys

PASTEBINS = ["https://0x0.st", "https://clbin.com"]

if len(sys.argv) != 2:
    print("Usage: python send_command.py <command>")
    sys.exit(1)

command = sys.argv[1]

for pastebin in PASTEBINS:
    try:
        if pastebin == "https://0x0.st":
            response = requests.post(pastebin, files={"f": command.encode()})
        else:
            response = requests.post(pastebin, data=command)

        if response.status_code == 200:
            url = response.text.strip()
            print(f"Command sent! {url}")

            # Save the URL for the laptop
            with open("last_command_url.txt", "w") as file:
                file.write(url)
            break  # Stop if successful
    except Exception as e:
        print(f"Failed to send via {pastebin}, trying next...")

else:
    print("All pastebin services failed. Try again later.")
