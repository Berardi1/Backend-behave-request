import requests
import jsonpath_ng as jp


def setup_request():
    return requests.Session()


def send_request(context, base_url, body, endpoint, method='GET', headers={}):
    headers = set_default_headers(headers)
    session = setup_request()
    full_url = base_url + endpoint

    try:
        if method == 'GET':
            response = session.get(full_url, headers=headers)
        elif method == 'POST':
            response = session.post(full_url, data=body, headers=headers)
        elif method == 'PUT':
            response = session.put(full_url, data=body, headers=headers)
        elif method == 'DELETE':
            response = session.delete(full_url, headers=headers)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")

        context.api_response_body = response.json()
        context.api_response_status_code = response.status_code
        context.api_response = response
        return response
    except Exception as e:
        # Handle exceptions or errors here
        raise e


def extract_value_from_json(response_body, json_path):
    try:
        jsonpath_expr = jp.parse(json_path)
        matches = [match.value for match in jsonpath_expr.find(response_body)]

        if matches:
            return matches[0]
        else:
            return None
    except Exception as e:
        # Handle exceptions or errors here
        raise e


def set_default_headers(headers={}):
    default_headers = {"Content-Type": "application/json"}
    default_headers.update(headers)
    return default_headers

