import requests

# Define the URL of your Tastypie API endpoint
api_url = 'http://127.0.0.1:8000/api/movies/'  # Replace with your API URL

# Make a GET request to the API endpoint
response = requests.get(api_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    print(data)
else:
    # Handle errors
    print(f"Failed to retrieve data. Status code: {response.status_code}")
