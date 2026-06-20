from locust import HttpUser, task, between
import random


class DummyJsonUser(HttpUser):

    host = "https://dummyjson.com"
    wait_time = between(1, 5)

    @task(5)
    def listar_produtos(self):
        with self.client.get(
            "/products",
            name="Listar Produtos",
            catch_response=True
        ) as response:

            if response.status_code == 200:
                response.success()
            else:
                response.failure(
                    f"Status inesperado: {response.status_code}"
                )
        

    @task(4)
    def consultar_produto(self):

        produto = random.randint(1, 30)

        with self.client.get(
            f"/products/{produto}",
            name="Consultar Produto",
            catch_response=True
        ) as response:

            if response.status_code == 200:
                response.success()
            else:
                response.failure(
                    f"Status inesperado: {response.status_code}"
                )


    @task(3)
    def listar_usuarios(self):
        with self.client.get(
            "/users",
            name="Listar Usuários",
            catch_response=True
        ) as response:

            if response.status_code == 200:
                response.success()
            else:
                response.failure(
                    f"Status inesperado: {response.status_code}"
                )
    

    @task(2)
    def login(self):
        with self.client.post(
            "/auth/login",
            json={
                "username": "emilys",
                "password": "emilyspass"
            },
            name="Login",
            catch_response=True
        ) as response:

            if response.status_code == 200:
                response.success()
            else:
                response.failure(
                    f"Falha no login: {response.status_code}"
                )

    @task(1)
    def criar_postagem(self):
        with self.client.post(
            "/posts/add",
            json={
                "title": "Teste de Performance",
                "userId": 1
            },
            name="Criar Postagem",
            catch_response=True
        ) as response:

            if response.status_code in [200, 201]:
                response.success()
            else:
                response.failure(
                    f"Falha ao criar postagem: {response.status_code}"
                )
        