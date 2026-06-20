from locust import HttpUser, task, between


class DummyJsonUser(HttpUser):

    host = "https://dummyjson.com"
    wait_time = between(1, 3)

    @task
    def listar_produtos(self):
        self.client.get("/products", name="Listar Produtos")

    @task
    def consultar_produto(self):
        self.client.get("/products/1", name="Consultar Produto")

    @task
    def listar_usuarios(self):
        self.client.get("/users", name="Listar Usuários")

    @task
    def login(self):
        self.client.post(
            "/auth/login",
            json={
                "username": "emilys",
                "password": "emilyspass"
            },
            name="Login"
        )

    @task
    def criar_postagem(self):
        self.client.post(
            "/posts/add",
            json={
                "title": "Teste Locust",
                "userId": 1
            },
            name="Criar Postagem"
        )