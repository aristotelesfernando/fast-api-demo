## EXEMPLO DE API FLASK COM CHAMADA MULTITHREAD

### 1- Crie um virtual enviroment para a aplicação
#### $ virtualenv venv
#### $ source venv/bin/activate 

### 2 - Instale as libs necessárias
#### $ pip install -r requirements.txt 

### A biblioteca FastAPI foi construida para funcionar de forma assincrona (ASGI)
### O GUNICORN implementa o padrão PEP 3333 WSGI e por este motivo os dois não são compatíveis.
### Para poder executar apropriadamente essa aplicação no Windows, recomendo que seja feito através de containers Docker
### 3 - Execute um build de uma imagem docker (todos os comandos a seguir são exemplos)
#### $ docker build -t <your_repo_name>/fast_api_demo:1.0 .
### 4 - Excute docker-compose
#### $ docker-compose up

### 5 - A api estará disponível na porta 8000 e o swagger pode ser acessado no endereço: http://127.0.0.1:8000/docs