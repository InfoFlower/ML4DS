#Fonction améliorée grâce à Chat GPT disponible sur VSCode
import requests
import os
import sys
import time

def get_wayback_urls(url):
    wayback_api = f"http://web.archive.org/cdx/search/cdx?url={url}&output=json&fl=timestamp,original&collapse=digest"
    response = requests.get(wayback_api)
    if response.status_code == 200:
        return response.json()[1:]  # Skip the header row
    else:
        print(f"Error fetching data from Wayback Machine: {response.status_code}")
        return []

def download_archive(timestamp, original_url, download_dir):
    archive_url = f"http://web.archive.org/web/{timestamp}/{original_url}"
    response = requests.get(archive_url)
    if response.status_code == 200:
        file_path = os.path.join(download_dir, f"{timestamp}.html")
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {archive_url} to {file_path}")
    else:
        print(f"Error downloading {archive_url}: {response.status_code}")

def main(url):
    download_dir = os.path.join(os.getcwd(), "wayback_downloads")
    os.makedirs(download_dir, exist_ok=True)

    archives = get_wayback_urls(url)
    existing_files = {f.split('.')[0] for f in os.listdir(download_dir) if f.endswith('.html')}
    for timestamp, original_url in archives:
        if timestamp not in existing_files:
            download_archive(timestamp, original_url, download_dir)
            time.sleep(20)  # Be nice to the Wayback Machine
        else : print(f'{timestamp} already downloaded')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scrapper.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    main(url)