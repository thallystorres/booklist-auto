# Booklist Auto

Automação de tarefas de web scraping em um site de vendas de livros utilizando a biblioteca Selenium.

## Descrição

Este projeto automatiza o processo de extração de dados de um site de vendas de livros, coletando informações relevantes e armazenando-as em um arquivo CSV. O objetivo é facilitar a obtenção de dados atualizados sobre livros disponíveis para venda.

## Funcionalidades

- Coleta Automatizada: Utiliza o Selenium para navegar no site e extrair dados dos livros.

- Armazenamento de Dados: Salva as informações coletadas em um arquivo `books.csv` para fácil acesso e análise.

## Estrutura do Projeto

- `main.py`: Script principal que executa o web scraping.

- `books.csv`: Arquivo gerado contendo os dados dos livros coletados.

- `requirements.txt`: Lista de dependências necessárias para executar o projeto.

## Tecnologias Utilizadas

**Python**: Linguagem principal utilizada no projeto.

**Selenium**: Biblioteca para automação de navegadores e web scraping.

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/thallystorres/booklist-auto.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd booklist-auto
    ```

3. Crie um ambiente virtual (opcional, mas recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use 'venv\Scripts\activate'
    ```

4. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Execute o script principal:

    ```bash
    python main.py
    ```

2. Verifique o arquivo books.csv para acessar os dados coletados.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.
