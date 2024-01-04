class Projeto:
    def __init__(self, requisito_programacao, requisito_design):
        self.requisito_programacao = requisito_programacao
        self.requisito_design = requisito_design


class Programador():
    # TODO: Complete o código do construtor inicializando os valores corretamente.
    def __init__(self, valor_por_projeto: int, habilidade_programacao: int):
        self.valor_por_projeto = valor_por_projeto
        self.habilidade_programacao = habilidade_programacao
        self.valor_recebido = 0

    # TODO: Um programador deve ser capaz de entregar um projeto se sua habilidade de programação é maior que o requisito de programação do projeto.
    def capaz(self, projeto: Projeto) -> bool:
        
        return self.habilidade_programacao >= projeto.requisito_programacao


class Designer():
    # TODO: Complete o código do construtor inicializando os valores corretamente.
    def __init__(self, valor_por_projeto: int, habilidade_design: int):
        self.valor_por_projeto = valor_por_projeto
        self.habilidade_design = habilidade_design
        self.valor_recebido = 0

    # TODO: Um designer deve ser capaz de entregar um projeto se sua habilidade de design é maior que o requisito de design do projeto.
    def capaz(self, projeto: Projeto) -> bool:

        return self.habilidade_design >= projeto.requisito_design
        


if __name__ == "__main__":

    valor, habilidade = map(int, input().split())
    programador = Programador(valor, habilidade)

    valor, habilidade = map(int, input().split())
    designer = Designer(valor, habilidade)

    n = int(input())
    for _ in range(n):
        requisito_programacao, requisito_design = map(int, input().split())
        projeto = Projeto(requisito_programacao, requisito_design)

        # TODO:Use os métodos das classes acima para calcular quando tanto o programador quanto o designer conseguem desenvolver o projeto P e dê a recompensa a cada um caso eles consigam.
        
        if programador.capaz(projeto) and designer.capaz(projeto):
            programador.valor_recebido += programador.valor_por_projeto
            designer.valor_recebido += designer.valor_por_projeto

    print(f"Programador: R$ {programador.valor_recebido}")
    print(f"Designer: R$ {designer.valor_recebido}")
