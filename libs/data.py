import httpx
from dotenv import load_dotenv
import os

load_dotenv()

def get_response():
    CLIENT_ID = os.getenv("CLIENT_ID") # Client ID from the API
    url = '<Request-url>' # URL of the API endpoint
    header = {'X-MAL-CLIENT-ID': CLIENT_ID}

    try:
        # Make a GET request to the API endpoint using requests.get()
        response = httpx.get(url, headers=header)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            return response.json()
        else:
            # Print the error status code if the request was unsuccessful
            print("Error status code:", response.status_code)
            return None
    
    except httpx.RequestError as e:
        # Handle any network-related errors or exceptions
        print("Error:", e)
        return None
    
def main():

    res = get_response()

    if res:
        # Print the number of responses
        print("Number of res:", len(res))
        # Print the first post
        print(res['data'][0])

    else:
        print("No res found")

if __name__ == "__main__":
    main()