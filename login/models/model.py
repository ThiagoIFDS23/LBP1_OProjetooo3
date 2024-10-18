class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

usuarios = [
    Usuario("admin", 'admin'),
    Usuario("user", 'user')
]