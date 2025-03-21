from pact import Verifier
from unittest import TestCase


class UserContractTest(TestCase):
    """
    Test to verify contract to jsonplaceholder and detect changes in https://jsonplaceholder.typicode.com/ API

    Useful when depending on external APIs that you have no control over.
    """

    def test_verify_provider(self):

        pact_file = "./testapp-jsonplaceholder.json"  # Path to the Pact contract
        # the contract gets automatically created when running the pact consumer part

        # The real provider url
        provider_url = "https://jsonplaceholder.typicode.com/"

        verifier = Verifier(
            "Provider",
            provider_base_url=provider_url,
        )

        # Run the verification of the contract against the real api
        verification_result, logs = verifier.verify_pacts(pact_file)

        self.assertEqual(verification_result, 0, f"Pact verification failed: {logs}")
