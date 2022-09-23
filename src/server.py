from flask import Flask
from repositories.database.InMemoryDatabase import InMemoryDatabase
from controllers.ExampleController import ExampleController
from services.ExampleService import ExampleService

# create Flask
app = Flask(__name__)

db = InMemoryDatabase()

# Creating Services and Injecting Database
example_service = ExampleService(db)

# Creating Controllers and Injecting Services
example_controller = ExampleController(example_service)

app.register_blueprint(example_controller.get_blueprint())

app.run()
