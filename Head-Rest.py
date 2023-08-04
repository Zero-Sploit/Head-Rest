import requests

def get_headers(url):
    try:
        response = requests.head(url)
        return response.headers
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while requesting {url}: {e}")
        return None

def append_https(url):
    if not url.startswith("https://") and not url.startswith("http://"):
        url = "https://" + url
    return url

def main():
    file_name = input("Enter the file name containing the list of URLs: ")

    try:
        with open(file_name, "r") as file:
            websites = file.read().splitlines()
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return

    for url in websites:
        url = append_https(url)
        headers = get_headers(url)
        if headers:
            print(f"Headers for {url}:")
            for key, value in headers.items():
                print(f"{key}: {value}")
            print("------------------------")
        else:
            print(f"Failed to retrieve headers for {url}")
            print("------------------------")

if __name__ == "__main__":
    main()
