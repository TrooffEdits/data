#!/bin/bash

UPLOAD_URL="https://0x0.st"

while true; do
    echo "Choose a command to send:"
    echo "a) Open browser on PC"
    echo "b) Play music"
    echo "c) Shutdown PC"
    echo "q) Quit"
    
    read -p "Enter your choice: " cmd

    if [[ "$cmd" == "q" ]]; then
        echo "Exiting..."
        break
    elif [[ "$cmd" =~ ^[a-c]$ ]]; then
        echo -n "$cmd" | curl -F'file=@-' $UPLOAD_URL | tee last_command_url.txt
        echo "Command sent!"
    else
        echo "Invalid choice, try again."
    fi
done
