@update
Feature: Update an existent post
    In order to update a existent post
    As a Jsonplaceholder user
    I want to be able to send a request to the API
    @smoke
    Scenario: Update a existent post
      When a 'PUT' request is sent to the endpoint 'posts/1' with body
    """
        {
          "userId": 2,
          "id": 2,
          "title": "update post test",
          "body": "This is an update of the test"
        }
    """

    Then the response body should have the 'userId' equals to '2'
    And the response body should have the 'id' equals to '2'
    And the response body should have the 'title' equals to 'update post test'
    And the response body should have the 'body' equals to 'This is an update of the test'