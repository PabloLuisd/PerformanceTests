from locust import HttpUser, task, between


class SauceDemoUser(HttpUser):

    host = "https://www.saucedemo.com"
    wait_time = between(1, 3)

    @task(3)
    def home_page(self):
        self.client.get("/")

    @task(1)
    def login_page(self):
        self.client.get("/")