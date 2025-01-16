import requests
from urllib.parse import urlparse

def validate_url(url):

    if not url.startswith(('http://','https://')):
        url = 'http://' + url
    parsed_url = urlparse(url)
    if not parsed_url.netloc:
        raise ValueError("Invalid URL format.")
    return url

def check_http_https(url):

    try:
        response = requests.get(url, timeout=5)
        if response.url.startswith('https://'):
            return 'HTTPS', True
        else:
            return 'HTTP', False
    except requests.RequestException as e:
        return f"Error: {e}", False

result = check_http_https("http://127.0.0.1:5000") #testing
print(result)  # Displays the returned value
