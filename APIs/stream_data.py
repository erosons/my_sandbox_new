import requests

def create_session_with_headers(headers):
    """
    Create a requests.Session with specified headers.
    
    Parameters:
    headers (dict): A dictionary of headers to use for the session.
    
    Returns:
    requests.Session: A configured session with the provided headers.
    """
    session = requests.Session()
    session.headers.update(headers)
    return session

def stream_data_from_api(session, url):
    """
    Stream data from the given API endpoint using the provided session.

    Parameters:
    session (requests.Session): The session to use for the request.
    url (str): The API endpoint URL.

    Yields:
    str: Lines of data streamed from the API.
    """
    try:
        with session.get(url, stream=True) as response:
            response.raise_for_status()  # Check for HTTP errors
            for line in response.iter_lines():
                if line:
                    yield line.decode('utf-8')
    except requests.RequestException as e:
        print(f'Error during request: {e}')

# Example usage
if __name__ == '__main__':
    headers = {
        'Authorization': 'Bearer your_token_here',
        'Accept': 'application/json',
        'User-Agent': 'your-app-name'
    }
    api_url = 'https://api.example.com/stream'

    # Create a session with headers
    session = create_session_with_headers(headers)

    # Stream data from the API
    for data in stream_data_from_api(session, api_url):
        print(data)
