from locust import HttpUser, task


class WordPressUser(HttpUser):

    @task
    def home(self):
        self.client.get("/")