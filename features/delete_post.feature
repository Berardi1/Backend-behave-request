@delete
Feature: Delete a post
    In order to delete a existent post
    As a Jsonplaceholder user
    I want to be able to send a request to the API

  @smoke
    Scenario: Delete an existent post
      When I perform a 'DELETE' request to the endpoint 'posts/1'
      Then the response status code should be: "204"