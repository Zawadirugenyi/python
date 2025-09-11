import requests
import os
from urllib.parse import urlparse

def fetch_image(url, downloaded_files):
    """Fetch and save a single image URL into Fetched_Images directory."""
    try:
        headers = {"User-Agent": "UbuntuFetcher/1.0"}
        response = requests.get(url, timeout=10, headers=headers)
        response.raise_for_status()

        # Check content type is image
        content_type = response.headers.get("content-type", "")
        if "image" not in content_type:
            print(f"✗ Skipping {url} (not an image).")
            return

        # Limit file size to 5 MB for safety
        max_size = 5 * 1024 * 1024
        content_length = int(response.headers.get("content-length", 0))
        if content_length and content_length > max_size:
            print(f"✗ Skipping {url} (file too large).")
            return

        # Extract filename
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        if not filename or "." not in filename:
            filename = "downloaded_image.jpg"

        # Avoid duplicates
        if filename in downloaded_files:
            print(f"↻ Already downloaded {filename}, skipping.")
            return

        filepath = os.path.join("Fetched_Images", filename)

        with open(filepath, "wb") as f:
            f.write(response.content)

        downloaded_files.add(filename)
        print(f"✓ Successfully fetched: {filename}")
        print(f"  Saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error fetching {url}: {e}")
    except Exception as e:
        print(f"✗ An error occurred fetching {url}: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Get URLs from user
    urls = input("Enter one or more image URLs separated by spaces:\n> ").split()

    # Create directory
    os.makedirs("Fetched_Images", exist_ok=True)

    downloaded_files = set()
    for url in urls:
        fetch_image(url.strip(), downloaded_files)

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
