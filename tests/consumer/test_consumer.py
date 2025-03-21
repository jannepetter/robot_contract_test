from pact import Consumer, Provider
from pact.matchers import Like, EachLike
from unittest import TestCase
from unittest.mock import patch
from tasks import user, all_users
from tests.expected.user import EXPECTED_USER
import atexit

pact = Consumer("Testapp").has_pact_with(Provider("JsonPlaceholder"))
pact.start_service()
atexit.register(pact.stop_service)


class SomeTest(TestCase):

    # mock tasks.py base url so it does not hit the real url but the default pact mock server http://localhost:1234
    @patch("tasks.BASE_URL", "http://localhost:1234/users/")
    def test_get_user(self):
        # Create a pact and test with pact to create the contract for the test -> consumer-provider.json
        # running the tests updates the contract if changes are made
        (
            pact.given("specific user")
            .upon_receiving("a request for specific user")
            .with_request("get", "/users/1")
            .will_respond_with(
                200,
                body=Like(EXPECTED_USER),
            )
        )

        with pact:
            result = user(1)

        self.assertEqual(
            result,
            {
                "id": 1,
                "name": "Sample User",
                "username": "sample_user",
                "email": "sample@user.com",
                "address": {
                    "street": "Elm Street",
                    "suite": "Apt. 789",
                    "city": "Springfield",
                    "zipcode": "12345-6789",
                    "geo": {"lat": "-37.3159", "lng": "81.1496"},
                },
                "phone": "1-555-123-4567 x98765",
                "website": "example.com",
                "company": {
                    "name": "TechFusion Inc.",
                    "catchPhrase": "Innovating the future of technology",
                    "bs": "empower digital transformation solutions",
                },
            },
        )

    @patch("tasks.BASE_URL", "http://localhost:1234/users/")
    def test_get_all_users(self):
        # Create a pact and test with pact to create the contract for the test -> consumer-provider.json
        (
            pact.given("all users")
            .upon_receiving("a request for users")
            .with_request("get", "/users/")
            .will_respond_with(
                200,
                body=EachLike(
                    EXPECTED_USER,
                    minimum=3,
                ),
            )
        )

        with pact:
            result = all_users()

        self.assertListEqual(
            result,
            [
                {
                    "id": 1,
                    "name": "Sample User",
                    "username": "sample_user",
                    "email": "sample@user.com",
                    "address": {
                        "street": "Elm Street",
                        "suite": "Apt. 789",
                        "city": "Springfield",
                        "zipcode": "12345-6789",
                        "geo": {"lat": "-37.3159", "lng": "81.1496"},
                    },
                    "phone": "1-555-123-4567 x98765",
                    "website": "example.com",
                    "company": {
                        "name": "TechFusion Inc.",
                        "catchPhrase": "Innovating the future of technology",
                        "bs": "empower digital transformation solutions",
                    },
                },
                {
                    "id": 1,
                    "name": "Sample User",
                    "username": "sample_user",
                    "email": "sample@user.com",
                    "address": {
                        "street": "Elm Street",
                        "suite": "Apt. 789",
                        "city": "Springfield",
                        "zipcode": "12345-6789",
                        "geo": {"lat": "-37.3159", "lng": "81.1496"},
                    },
                    "phone": "1-555-123-4567 x98765",
                    "website": "example.com",
                    "company": {
                        "name": "TechFusion Inc.",
                        "catchPhrase": "Innovating the future of technology",
                        "bs": "empower digital transformation solutions",
                    },
                },
                {
                    "id": 1,
                    "name": "Sample User",
                    "username": "sample_user",
                    "email": "sample@user.com",
                    "address": {
                        "street": "Elm Street",
                        "suite": "Apt. 789",
                        "city": "Springfield",
                        "zipcode": "12345-6789",
                        "geo": {"lat": "-37.3159", "lng": "81.1496"},
                    },
                    "phone": "1-555-123-4567 x98765",
                    "website": "example.com",
                    "company": {
                        "name": "TechFusion Inc.",
                        "catchPhrase": "Innovating the future of technology",
                        "bs": "empower digital transformation solutions",
                    },
                },
            ],
        )
