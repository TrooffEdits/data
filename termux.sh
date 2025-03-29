CMD="a"  # Change this to whatever command you want
URL=$(echo -n "$CMD" | curl -s -X POST -d @- https://paste.rs)
echo "$URL" > last_command_url.txt
