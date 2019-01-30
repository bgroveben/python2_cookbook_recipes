Feature: Handle storing, retrieving and deleting customer details
Scenario: Retrieve a customers details
Given some users are in the system
When I retrieve the customer 'david01'
Then I should get a '500' response
And the following user details are returned:
| name |
| David Sale |
