# Use a imagem oficial do PostgreSQL como base
FROM postgres:latest
# Variáveis de ambiente para configurar o banco de dados
ENV POSTGRES_DB=dev-web
ENV POSTGRES_USER=admin
ENV POSTGRES_PASSWORD=12341234
# Copie o arquivo SQL de criação de tabelas para dentro do contêiner
COPY tables.sql /docker-entrypoint-initdb.d/
