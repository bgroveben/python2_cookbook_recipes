Feature: Handle storing, retrieving and deleting customer details

# Comments follow a hash sign and start on a new line
# https://docs.cucumber.io/gherkin/reference/

Scenario: Retrieve a customers details
Given some users are in the system
When I retrieve the customer 'david01'
Then I should get a '200' response
And the following user details are returned:
| name |
| David Sale |
