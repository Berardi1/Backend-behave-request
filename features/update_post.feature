Feature: Update an existent post
    In order to update a existent post
    As a Jsonplaceholder user
    I want to be able to send a request to the API


    Scenario: Update a existent post
      When a "PUT" request is sent to the endpoint 'posts/1' with body:
    """
        {
          "userId": 2
          "id": 2
          "title": "update POST test"
          "body": "This is an update of the test"
        }
    """

    Then the response should have the "userId" equals to "10"
    And the response should have then "id" equals to "8"
    And the response should have the  "title" equals to "update POST test"
    And the response should have the "body" equals to "This is an update of the test"