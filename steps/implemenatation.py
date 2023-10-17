from behave import when, then
from support import api_request


@when(u"I perform a '{method}' request to the endpoint '{endpoint}'")
def step_impl(context, method, endpoint):
    api_request.send_request(context=context, method=method, base_url=context.config.userdata['base_url'], endpoint=endpoint, body=context.text)


@then(u"the response body should have the '{response_path}' equals to '{expected_response_value}'")
def step_impl(context, response_path, expected_response_value):
    obtained_value = api_request.get_response_value(context.api_response_body, response_path)
    assert obtained_value != False, 'Response value was not found in response: %s' % context.api_response_body
    assert str(obtained_value) == expected_response_value, 'Response value not expected: %s not equal to %s' % (expected_response_value, obtained_value)


@then(u'the response status code should be: "{expected_status_code}"')
def step_impl(context, expected_status_code):
    assert expected_status_code == context.api_response_status_code, f"Expected status code %s, but got %s" % (expected_status_code, context.api_response_status_code)


@when(u"a '{method}' request is sent to the endpoint '{endpoint}' with body")
def step_impl(context, method, endpoint):
    api_request.send_request(context, base_url=context.config.userdata['base_url'], endpoint=endpoint, method=method, body=context.text)