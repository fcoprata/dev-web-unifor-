Para construir a imagem
```docker build -t myapp .```

Para executar a imagem
```docker run --name myapp_container -d -p 5432:5432 myapp```

Informações da conexão está no Dockerfile
