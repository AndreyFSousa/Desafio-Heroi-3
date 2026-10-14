
class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo.lower() == "mago":
            ataque = "magia"
        elif self.tipo.lower() == "guerreiro":
            ataque = "espada"
        elif self.tipo.lower() == "monge":
            ataque = "artes marciais"
        elif self.tipo.lower() == "ninja":
            ataque = "shuriken"
        else:
            ataque = "um ataque desconhecido"

        print(f"O {self.tipo} atacou usando {ataque}")


heroi1 = Heroi("Gandalf", 1000, "mago")
heroi2 = Heroi("Aragorn", 35, "guerreiro")
heroi3 = Heroi("Shaolin", 40, "monge")
heroi4 = Heroi("Hattori", 25, "ninja")

heroi1.atacar()
heroi2.atacar()
heroi3.atacar()
heroi4.atacar()
