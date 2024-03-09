Construir a network unindo os container: 
```docker network create minha-rede```


Para construir a imagem postgres
```docker build -t mypostgresdb .```

Para executar a imagem postgres 
```docker run -d -p 5432:5432 --name meu-postgresdb mypostgresdb```

Para construir a imagem api
```docker build -t myflaskapp -f Dockerfile .```

Para executar a imagem api 
```docker run -d -p 9000:9000 --name meu-flaskapp myflaskapp```

Informações da conexão está no Dockerfile

Seguinte comando no terminal para instalar as dependências dentro da pasta do back-end localmente (caso não use o docker):
```pip install -r requirements.txt```