from locust import HttpUser, task, between


class DummyJsonUser(HttpUser):

    host = "https://dummyjson.com"
    wait_time = between(1, 3)

    @task(5)
    def listar_produtos(self):
        self.client.get(
            "/products",
            name="Listar Produtos"
        )

    @task(4)
    def consultar_produto(self):
        self.client.get(
            "/products/1",
            name="Consultar Produto"
        )

    @task(3)
    def listar_usuarios(self):
        self.client.get(
            "/users",
            name="Listar Usuários"
        )

    @task(2)
    def login(self):
        self.client.post(
            "/auth/login",
            json={
                "username": "emilys",
                "password": "emilyspass"
            },
            name="Login"
        )

    @task(1)
    def criar_postagem(self):
        self.client.post(
            "/posts/add",
            json={
                "title": "Teste de Performance",
                "userId": 1
            },
            name="Criar Postagem"
        )