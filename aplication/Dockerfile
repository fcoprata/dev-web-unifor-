# Use uma imagem base do Python
FROM python:3.9-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos necessários para o diretório de trabalho no container
COPY . .

# Instala as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Exponha a porta em que a API estará em execução
EXPOSE 9000

# Comando para iniciar a aplicação (se a API estiver em app.py)
CMD ["python", "app.py"]
