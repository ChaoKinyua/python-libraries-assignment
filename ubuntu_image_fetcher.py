import os
import requests
from urllib.parse import urlparse

def fetch_image():
    # Prompt the user for the image URL
    url = input("🌍 Please enter an image URL: ").strip()

    # Create directory if it doesn't exist
    directory = "Fetched_Images"
    os.makedirs(directory, exist_ok=True)

    try:
        # Fetch the image
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise error for bad status codes

        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        if not filename:  # If URL doesn’t have a filename, generate one
            filename = "fetched_image.jpg"

        filepath = os.path.join(directory, filename)

        # Save the image in binary mode
        with open(filepath, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)

        print(f"✅ Image successfully fetched and saved as {filepath}")

    except requests.exceptions.HTTPError as http_err:
        print(f"⚠️ HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("⚠️ Connection error. Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("⚠️ Request timed out. Try again later.")
    except Exception as err:
        print(f"⚠️ An error occurred: {err}")

if __name__ == "__main__":
    fetch_image()
