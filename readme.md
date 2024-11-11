# API Flask com Redis e MySQL

## Introdução ao Projeto

Este projeto é uma API desenvolvida com Flask e integrada ao Redis e MySQL, criada para explorar o uso de cache com Redis para otimização de consultas. A aplicação permite criar e buscar produtos, armazenando dados em cache para reduzir o tempo de resposta em operações de busca.

## Tecnologias Utilizadas

- **Flask**: Framework principal para criação da API.
- **SQLAlchemy**: ORM para gerenciar a comunicação com o banco de dados MySQL.
- **MySQL**: Banco de dados relacional para persistência dos dados dos produtos.
- **Redis**: Utilizado como sistema de cache para otimização de buscas de produtos.
- **Pytest**: Framework para testes automatizados.
- **Docker**: Para facilitar o ambiente de desenvolvimento e a execução dos serviços.

## Funcionalidades

A API possui as seguintes funcionalidades:

- **Criar Produto**: Cria um novo produto no banco de dados MySQL e armazena-o também no cache Redis.
- **Buscar Produto**: Busca um produto no cache Redis. Se não encontrado no cache, realiza a busca no banco de dados, armazena o resultado no cache e o retorna.

## Rotas

| Método | Endpoint                      | Descrição                        |
| ------ | ----------------------------- | -------------------------------- |
| POST   | `/products/create`            | Cria um novo produto.            |
| GET    | `/products/find-product/<id>` | Busca um produto pelo seu ID.    |

### Exemplos de uso

1. **Criar Produto**
   - **URL**: `/products/create`
   - **Método**: POST
   - **Body**:
     ```json
     {
       "name": "Produto A",
       "price": "19.99",
       "quantity": 10
     }
     ```
   - **Resposta**: 
     ```json
     {
       "msg": "Produto inserido com sucesso!"
     }
     ```

2. **Buscar Produto**
   - **URL**: `/products/find-product/<id>`
   - **Método**: GET
   - **Resposta**:
     ```json
     {
       "name": "Produto A",
       "price": "19.99",
       "quantity": 10
     }
     ```

## Como Rodar o Projeto

### Pré-requisitos
- Python 3.8 ou superior
- MySQL
- Redis
- Ambiente virtual (recomendado)

### Passo a Passo

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/Dav1dSo/api-redis.git
    cd sua-repositorio
    ```

2. **Crie e ative o ambiente virtual**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3. **Instale as dependências**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure o banco de dados MySQL**:
    - Crie um banco de dados MySQL para a aplicação.
    - Configure as variáveis de ambiente necessárias para a conexão com o MySQL (`DB_HOST`, `DB_USER`, `DB_PASSWORD`, `DB_NAME`).

5. **Configure o Redis**:
    - Certifique-se de que o Redis está em execução localmente ou configure as variáveis de ambiente para a conexão (`REDIS_HOST`, `REDIS_PORT`).

6. **Execute as migrações (se aplicável)**:
    - Se o projeto utiliza migrações com SQLAlchemy, rode as migrações necessárias para preparar o banco de dados.

7. **Execute os testes**:
    ```bash
    pytest
    ```

8. **Inicie o servidor**:
    ```bash
    flask run
    ```

Agora o projeto estará disponível em `http://127.0.0.1:5000`.