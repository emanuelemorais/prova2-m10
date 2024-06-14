# Prova 2 - módulo 10
## Emanuele Lacerda Morais Martins
Atividade realizada durante prova 2 do módulo 10 de engenharia da computação.

## Como rodar usando docker e nginx

1. Clone esse repositório
2. Entre no diretório `prova2-m10/src`
3. Rode no terminal o comando abaixo:
```
docker compose up
```
Isso irá construir o container, o output será como o da imagem abaixo:
<img src="Screenshot 2024-06-14 at 10.49.37.png">

4. Acesse a documentação da API no navegador:
```
http://localhost/docs
```

## Log

O Log foi mapeado para um arquivo fora do container, ele pode ser encontrado em:
```
prova2-m10/src/systemlog.log
```

## Docs Insomnia

A documentação da API também pode ser acessada pelo Insomnia usando o arquivo `Insomnia_Prova2.json` na raiz do repositório.