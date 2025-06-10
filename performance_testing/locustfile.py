from locust import HttpUser, task, between

class WebTestUser(HttpUser):
    wait_time = between(1, 3)  # her isteğin arası 1-3 saniye

    @task
    def open_form_page(self):
        self.client.get("/text-box")  # sayfa istek testi
