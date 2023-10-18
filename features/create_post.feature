@create
Feature: Create a post
    As a Jsonplaceholder user
    I want to be able to send a request to the API

  @smoke
  Scenario: Verify that API successfully creates a new post
    When a 'POST' request is sent to the endpoint 'posts' with body
    """
        {
          "userId": 1,
          "id": 2,
          "title": "POST test",
          "body": "This is a test"
        }
    """
    Then the response body should have the 'userId' equals to '1'
    And the response body should have the 'id' equals to '2'
    And the response body should have the 'title' equals to 'POST test'
    And the response body should have the 'body' equals to 'This is a test'