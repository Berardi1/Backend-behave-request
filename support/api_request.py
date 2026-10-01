import requests


def setup_request():
    return requests.Session()


def send_request(context, base_url, endpoint, body, headers=None, method='GET'):
    if headers is None:
        headers = {}

    headers = set_default_headers(headers)

    session = setup_request()
    full_url = base_url + endpoint

    methods = {
        'get': session.get,
        'post': session.post,
        'put': session.put,
        'delete': session.delete,
        'head': session.head,
        'options': session.options
    }

    request_method = methods[method.lower()]

    if method.lower() in ['post', 'put']:
        response = request_method(full_url, data=body, headers=headers)
    else:
        response = request_method(full_url, headers=headers)

    context.api_response_body = response.json()
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
