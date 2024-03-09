# Use a imagem base do Python
FROM python:3.9-slim
# Defina o diretório de trabalho como /app
WORKDIR /app
# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .
# Instale as dependências
RUN pip install -r requirements.txt
# Copie todo o conteúdo da pasta back para o diretório de trabalho no contêiner
COPY . .
# Exponha a porta 9000 para a aplicação Flask
EXPOSE 9000
# Comando para iniciar o servidor Flask
CMD ["python", "app.py"]
