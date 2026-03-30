"""
Projeto: classificador simples de mensagens de suporte

Como funciona:
- usa regras por palavras-chave
- compara o texto digitado com categorias conhecidas
- escolhe a categoria com maior pontuação

Categorias do exemplo:
- login
- vistoria
- entrega_chaves
- chamado
- financeiro
"""

from dataclasses import dataclass
from typing import Dict, List, Tuple
import re


@dataclass
class ResultadoClassificacao:
    texto: str
    categoria: str
    pontuacao: int
    palavras_encontradas: List[str]


class ClassificadorSimplesIA:
    def __init__(self) -> None:
        self.categorias: Dict[str, List[str]] = {
            "login": [
                "login",
                "senha",
                "acesso",
                "entrar",
                "portal",
                "token",
                "qr code",
                "codigo",
                "autenticacao",
            ],
            "vistoria": [
                "vistoria",
                "revisoria",
                "agendar",
                "reagendar",
                "agenda",
                "unidade",
                "inspecao",
                "cliente",
                "sincronizacao",
                "sincronização",
            ],
            "entrega_chaves": [
                "chaves",
                "chave",
                "entrega",
                "link",
                "copiar link",
                "reenviar",
                "proprietario",
            ],
            "chamado": [
                "chamado",
                "erro",
                "anexo",
                "anexos",
                "arquivo",
                "painel",
                "solicitacao",
                "tecnico",
                "salvar",
            ],
            "financeiro": [
                "boleto",
                "pagamento",
                "financeiro",
                "cobranca",
                "valor",
                "relatorio",
                "divergencia",
                "taxa",
            ],
            "manutencao": [
            "manutenção",
            "manutencao",
            "preventiva",
            "plano",
            "planos",
            "sistema construtivo",
            "construtivo",
            "empreendimento",
            ],
            "chamado": [
            "chamado",
            "erro",
            "anexo",
            "arquivo",
            "painel",
            "solicitacao",
            "tecnico",
            "salvar",
            "excluir",
            "remover",
            ],
        }

    def normalizar_texto(self, texto: str) -> str:
        texto = texto.lower().strip()
        texto = re.sub(r"[^a-zA-ZÀ-ÿ0-9\s]", " ", texto)
        texto = re.sub(r"\s+", " ", texto)
        return texto

    def classificar(self, texto: str) -> ResultadoClassificacao:
        texto_normalizado = self.normalizar_texto(texto)
        pontuacoes: Dict[str, Tuple[int, List[str]]] = {}

        for categoria, palavras_chave in self.categorias.items():
            pontos = 0
            encontradas: List[str] = []

            for palavra in palavras_chave:
                if palavra in texto_normalizado:
                    pontos += 1
                    encontradas.append(palavra)

            pontuacoes[categoria] = (pontos, encontradas)

        melhor_categoria = "nao_identificada"
        melhor_pontuacao = 0
        melhores_palavras: List[str] = []

        for categoria, (pontos, encontradas) in pontuacoes.items():
            if pontos > melhor_pontuacao:
                melhor_categoria = categoria
                melhor_pontuacao = pontos
                melhores_palavras = encontradas

        return ResultadoClassificacao(
            texto=texto,
            categoria=melhor_categoria,
            pontuacao=melhor_pontuacao,
            palavras_encontradas=melhores_palavras,
        )

    # Função de exemplos removida para deixar o terminal mais limpo


def menu() -> None:
    ia = ClassificadorSimplesIA()

    print("=" * 60)
    print("SISTEMINHA DE IA - CLASSIFICADOR SIMPLES SEM BIBLIOTECAS")
    print("=" * 60)

    # ia.mostrar_exemplos()  # desativado para não poluir o terminal

    while True:
        print("Digite uma mensagem para classificar.")
        print("Digite 'sair' para encerrar.")
        texto = input("\nMensagem: ").strip()

        if texto.lower() == "sair":
            print("Encerrando o sistema. Até mais!")
            break

        if not texto:
            print("Digite algum texto válido.\n")
            continue

        resultado = ia.classificar(texto)

        print("\n--- RESULTADO ---")
        print(f"Categoria prevista: {resultado.categoria}")
        print(f"Pontuação: {resultado.pontuacao}")
        print(
            "Palavras encontradas: "
            f"{', '.join(resultado.palavras_encontradas) if resultado.palavras_encontradas else 'nenhuma'}"
        )
        print()


if __name__ == "__main__":
    menu()
