Feature: Create a post
    As a Jsonplaceholder user
    I want to be able to send a request to the API

  @current
  Scenario: Verify that API successfully creates a new post
    When When a 'POST' request is sent to the endpoint 'posts/1' with body
    """
        {
          "userId": 1
          "id": 2
          "title": "POST test"
          "body": "This is a test"
        }
    """
    Then the response should have the 'userId' equals to '1'
    And the response should have the 'id' equals to '2'
    And the response should have the 'title' equals to 'POST test'
    And the response should have the 'body' equals to 'This is a test'