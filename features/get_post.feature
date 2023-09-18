@get_post
Feature: Getting a post
    As a Jsonplaceholder user
    I want to request the API



     Scenario: Validate that API returns the correct post information
       When I perform a 'GET' request to the endpoint 'posts/1'
       Then the response should have the 'userId' equals to '1'
       And the response should have the 'id' equals to '1'

