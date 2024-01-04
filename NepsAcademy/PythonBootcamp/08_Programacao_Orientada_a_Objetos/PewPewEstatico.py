class Inimigo:
    quantidade_vivos: int
    quantidade_mortos = 0

    # Crie um construtor que inicializa um inimigo usando os parâmetros abaixo.
    def __init__(self, id: int, X: int, Y: int, vivo: bool):
        self.id = id
        self.x = X
        self.y = Y
        self.vivo = vivo

    # Método que muda a o status do inimigo de vivo para morto caso seja acertado pelo lazer na posição (X,Y). Também deve atualizar a variável quantidade_vivos.
    def foi_acertado(self, X: int, Y: int) -> None:
        if self.x == X and self.y == Y and self.vivo:
            self.vivo = False
            Inimigo.quantidade_vivos -= 1
            Inimigo.quantidade_mortos += 1


if __name__ == "__main__":

    n = int(input())

    inimigos = []
    Inimigo.quantidade_vivos = n

    for id in range(n):
        x, y = map(int, input().split())
        inimigos.append(Inimigo(id, x, y, True))

    m = int(input())

    for i in range(m):
        x, y = map(int, input().split())

        for inimigo in inimigos:
            inimigo.foi_acertado(x, y)

    # Imprima a saída conforme indicada no enunciado do exercício.
    print("vivos:", Inimigo.quantidade_vivos)
    print("mortos:", Inimigo.quantidade_mortos)

