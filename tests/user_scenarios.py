from locust import HttpUser, task, between
from .utils import ENDPOINTS


class ReadOnlyUser(HttpUser):
    """
    Simulates a user that only browses data (GET requests).
    Good for testing read-heavy scenarios.
    """
    wait_time = between(1, 3)

    @task(3)
    def list_posts(self):
        self.client.get(ENDPOINTS["get_posts"], name="GET /posts")

    @task(2)
    def list_users(self):
        self.client.get(ENDPOINTS["get_users"], name="GET /users")

    @task(1)
    def get_single_post(self):
        self.client.get(ENDPOINTS["get_post"], name="GET /posts/1")


class WriteHeavyUser(HttpUser):

    wait_time = between(2, 5)

    @task(4)
    def create_post(self):
        payload = {
            "title": "performance-test-post",
            "body": "Created by Locust performance test.",
            "userId": 1
        }
        self.client.post(
            ENDPOINTS["create_post"],
            json=payload,
            name="POST /posts"
        )

    @task(1)
    def read_after_write(self):
        self.client.get(ENDPOINTS["get_posts"], name="GET /posts")
