# Use a imagem oficial do Python para o FastAPI
FROM python:3.9-slim

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia os arquivos do back-end para o contêiner
COPY . /app

# Instala as dependências do back-end
RUN pip install -r requirements.txt

# Instala o servidor web Nginx para servir o front-end
RUN apt-get update && apt-get install -y nginx

# Copia o index.html para dentro do diretório onde o Nginx servirá os arquivos estáticos
COPY index.html /usr/share/nginx/html/

# Copia a configuração do Nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Expõe a porta do servidor HTTP do Nginx
EXPOSE 80

# Comando para iniciar o servidor FastAPI e o Nginx
CMD service nginx start && uvicorn app:app --host 0.0.0.0 --port 9000
