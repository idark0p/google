import requests

# Define the URL of the chat endpoint
url = 'http://localhost:8000/chat/'

# Define the user's message
user_message = "Hello, chatbot!"

# Send a POST request with the user's message
response = requests.post(url, json={"text": user_message})

# Print the response
print(response.json())
server {
    listen 80;
    server_name 18.116.199.161;
    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}