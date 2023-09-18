from behave import when, then
from steps import api_request


@when(u"I perform a '{method}' request to the endpoint '{endpoint}'")
def step_impl(context, method, endpoint):
    api_request.send_request(context, base_url=context.config.userdata['base_url'], endpoint=endpoint, method=method)


@then(u"the response should have the '{response_path}' equals to '{expected_response_value}'")
def step_impl(context, response_path, expected_response_value):
    extracted_values = api_request.extract_value_from_json(context.api_response_body, response_path)

    if extracted_values is None:
        raise AssertionError(f"No matches found for JSONPath: {response_path}")

    if str(extracted_values) != expected_response_value:
        raise AssertionError(
            f"Expected '{response_path}' to be '{expected_response_value}', but got '{extracted_values}'"
        )


@then(u'the response status code should be: "{expected_status_code}"')
def step_impl(context, expected_status_code):
    expected_status_code = int(expected_status_code)
    response = context.api_response
    assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}"


@when(u"When a '{method}' request is sent to the endpoint '{endpoint}' with body")
def step_impl(context, method, endpoint):
    api_request.send_request(context, base_url=context.config.userdata['base_url'], endpoint=endpoint, method=method, body=context.text)