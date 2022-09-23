from flask import Flask
from controllers.OrderController import OrderController
from repositories.database.InMemoryDatabase import InMemoryDatabase
from controllers.ExampleController import ExampleController
from services.ExampleService import ExampleService
from services.OrderService import OrderService

# create Flask
app = Flask(__name__)

db = InMemoryDatabase()

# Creating Services and Injecting Database
example_service = ExampleService(db)
order_service = OrderService(db)

# Creating Controllers and Injecting Services
example_controller = ExampleController(example_service)
order_controller = OrderController(order_service)

app.register_blueprint(example_controller.get_blueprint())
app.register_blueprint(order_controller.get_blueprint())


app.run()
