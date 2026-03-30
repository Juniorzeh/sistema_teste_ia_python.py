Classificador de Chamados com Python (Sem Bibliotecas de IA)

📖 Descrição

Este projeto é um classificador simples de mensagens de suporte desenvolvido em Python puro.

A aplicação recebe um texto e classifica automaticamente em categorias como:

login
vistoria
entrega de chaves
chamado
financeiro

O objetivo é demonstrar a lógica base de sistemas de classificação semelhantes aos utilizados em IA, 
sem utilizar bibliotecas externas como scikit-learn ou numpy.

⚙️ Como funciona

O sistema utiliza uma abordagem baseada em palavras-chave:

O texto é normalizado (convertido para minúsculo e sem caracteres especiais)
Cada categoria possui uma lista de palavras associadas
O sistema verifica quais palavras aparecem no texto informado
Cada correspondência soma pontos para a categoria
A categoria com maior pontuação é selecionada

Caso nenhuma palavra seja encontrada, o sistema retorna como não identificado.

🚀 Como executar
1. Clone o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git
2. Acesse a pasta
cd seu-repositorio
3. Execute o projeto
python sistema_teste_ia_python.py

🧪 Exemplo de uso

Entrada:

não consigo acessar o portal

Saída:

Categoria prevista: login
Pontuação: 2
Palavras encontradas: acesso, portal

🎯 Objetivo

Este projeto foi criado com foco em aprendizado e prática de:

Python básico
Estrutura de classes
Manipulação de strings
Lógica de classificação
Fundamentos de IA

🚧 Próximos passos

Implementar versão com scikit-learn
Criar API com Flask
Adicionar interface web
Melhorar algoritmo de classificação

💡 Observação

Este projeto não utiliza machine learning, mas sim regras simples baseadas em palavras-chave. 
Ele serve como base para entender como sistemas de classificação funcionam antes de utilizar bibliotecas de IA mais avançadas.
