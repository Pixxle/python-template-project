# template-project-python
![Tests](https://github.com/pixxle/python-template-project/actions/workflows/tests.yml/badge.svg)
![Linting](https://github.com/pixxle/python-template-project/actions/workflows/lint.yml/badge.svg)

👋 Hello peeps!

I got tired of always creating this application layout time and time again 😅
So decided to just create a template that's easily used for starting new python projects and throw it up here on Github.

Quick explaination of folder structure:
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

This project is loosly based on [Uncle bobs clean architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html) but doesn't use is-a relationships via inheritance, instead by using @abc.abstractclassmethod we simulate something very similar to interface implementation in other languages, such as Go or Java :) This is the cleanest way I've found to implement is-a relationship without getting into a inheritance hell. 👿
