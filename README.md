# template-project-python

Some explanations of what each package does:

```
.
├── examples # http request examples for trying the application out
├── src
│   ├── controllers # providers routes and handles incoming/outgoing requests
│   ├── dtos # Transfer Objects
│   ├── models # Implements core business logic
│   ├── pkg # Common modules available for usage
│   ├── repositories # Each repository would implement some type of "outside connection", could be database, could be sqs for example.
│   │   ├── database # Contains interface definition for database and database implementation
│   └── services # Service lives between controllers and repository, uses repositories to call "outside connection" without knowing anything about the implementation of that connection.
├── tests
│   └── src
│       └── services # examples of how unit tests would be implemented
```
