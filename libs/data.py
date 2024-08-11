import requests
from requests.exceptions import RequestException

def get_posts():
    url = 'https://api.myanimelist.net/v2/anime?q=one&limit=4'

    try:
        # Make a GET request to the API endpoint using requests.get()
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            return response.json()
        else:
            # Print the error status code if the request was unsuccessful
            print("Error status code:", response.status_code)
            return None
    
    except RequestException as e:
        # Handle any network-related errors or exceptions
        print("Error:", e)
        return None
    
def main():

    posts = get_posts()

    if posts:
        # Print the number of posts
        print("Number of posts:", len(posts))
        # Print the first post
        print("First post:", posts[0])

    else:
        print("No posts found")

if __name__ == "__main__":
    main()