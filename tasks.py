from robocorp.tasks import task
import requests

BASE_URL = "https://jsonplaceholder.typicode.com/users/"

# v0.1


def user(id):
    """Fetch a user object by user_name from the server."""
    uri = BASE_URL + str(id)
    return requests.get(uri).json()


def all_users():
    """Fetch a user object by user_name from the server."""
    uri = BASE_URL
    return requests.get(uri).json()


@task
def minimal_task():
    user_data = user(1)
    message = "Hello"
    message = message + f" {user_data["name"]}!"
    print(message)
