import subprocess

def showrun():
    # read https://www.datacamp.com/tutorial/python-subprocess to learn more about subprocess
    command = ['ansible-playbook', 'playbook.yaml']
    result = subprocess.run(command, capture_output=True, text=True)
    result_output = result.stdout
    if 'ok=2' in result_output:
        # Construct the filename
        filename = f"show_run_65070099_CSR1KV-Pod1-2.txt"  # Replace with your student ID and router name

        # Check if the file exists
        if os.path.exists(filename):
            # Send the file to the Webex Team room
            send_file_to_webex(filename)
            return filename
    else:
        # Send error message to Webex Team room
        send_message_to_webex('Error: Ansible')
        return 'Error: Ansible'

def send_file_to_webex(filename):
    url = "https://webexapis.com/v1/messages"
    headers = {
        "Authorization": os.environ.,
        "Content-Type": "application/json"
    }
    data = {
        "roomId": "<YOUR_ROOM_ID>",
        "text": f"Attached file: {filename}"
    }
    # Upload the file as well
    files = {'file': open(filename, 'rb')}
    response = requests.post(url, headers=headers, data=data, files=files)

def send_message_to_webex(message):
    url = "https://webexapis.com/v1/messages"
    headers = {
        "Authorization": os.environ.,
        "Content-Type": "application/json"
    }
    data = {
        "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNTFmNTJiMjAtNWQwYi0xMWVmLWE5YTAtNzlkNTQ0ZjRkNGZi",
        "text": message
    }
    requests.post(url, headers=headers, json=data)

# Call the function
showrun()