# Dockerfile para o backend Flask

# Use a imagem base do Python
FROM python:3.9-slim

# Defina o diretório de trabalho como /app
WORKDIR /app

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY back/requirements.txt .

# Instale as dependências
RUN pip install -r requirements.txt

# Copie todo o conteúdo da pasta back para o diretório de trabalho no contêiner
COPY back/ .

# Exponha a porta 8000 para a aplicação Flask
EXPOSE 9000

# Comando para iniciar o servidor Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "9000"]

# Dockerfile para o PostgreSQL

# Use a imagem oficial do PostgreSQL como base
FROM postgres:latest

# Variáveis de ambiente para configurar o banco de dados
ENV POSTGRES_DB=dev-web
ENV POSTGRES_USER=admin
ENV POSTGRES_PASSWORD=12341234

# Copie o arquivo SQL de criação de tabelas para dentro do contêiner
COPY tables.sql /docker-entrypoint-initdb.d/
