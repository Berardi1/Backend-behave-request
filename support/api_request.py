import requests


def setup_request():
    return requests.Session()


def send_request(context, base_url, endpoint, body, headers={}, method='GET'):
    # Set default headers for the request
    headers = set_default_headers(headers)

    # Create a session for making the HTTP request
    session = setup_request()

    # Construct the full URL by combining the base URL and endpoint
    full_url = base_url + endpoint

    # Define available HTTP methods and execute the requested method
    methods = {
        'get': session.get(full_url, headers=headers),
        'post': session.post(full_url, data=body, headers=headers),
        'put': session.put(full_url, data=body, headers=headers),
        'delete': session.delete(full_url, headers=headers),
        'head': session.head(full_url, headers=headers),
        'options': session.options(full_url, headers=headers)
    }
    response = methods[method.lower()]  # Execute the requested HTTP method

    # Store the response body and status code in the context
    context.api_response_body = response.json()  # Parse response JSON
    context.api_response_status_code = response.status_code


def get_response_value(response_body, value_path):
    """
        Retrieve a specific value from a JSON response using a path.

        This function navigates a JSON response and retrieves a specific value
        using a provided path. If the value exists, it is returned; otherwise,
        False is returned.
    """

    search_values = value_path.split('/')
    value_found = response_body
    for value in search_values:
        # Check if found last iterable item in the json path
        try:
            if value in value_found:
                value_found = value_found[value]
                continue
            return False
        except TypeError:
            return False
    return value_found


def set_default_headers(headers={}):
    """
        Set default HTTP headers with the option to extend or override them.

        This function creates a dictionary of default HTTP headers with
        'Content-Type' set to 'application/json'. If additional headers are
        provided, they will be merged into the default headers dictionary,
        allowing you to extend or override the defaults.
    """

    default_headers = {"Content-Type": "application/json"}
    default_headers.update(headers)
    return default_headers
