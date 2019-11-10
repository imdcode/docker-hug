# Ambiente para a programação de APIs utilizando python hug 

Esta imagem docker foi desenvolvida no âmbito da disciplina MPES0029 Infraestrutura de TI para as atividades de desenvolvimento de APIs REST utilizando o módulo python hug (https://www.hug.rest/).

## Preparando o ambiente

### Criando a imagem docker

Para criar a imagem docker a partir do Dockerfile, utilize o comando a seguir. A imagem será nomeada como "docker-hug:1.0".

```
docker build -t docker-hug:1.0 .
```

### Instanciando o container

Uma vez que a imagem tenha sido construída com sucesso no passo anterior, agora é possível instanciar um container. Para isso, utilize o comando a seguir.

```
docker run -it --name mpti2019 -p 8000:8000 -v /Users/silviocs/hug_api/docker-hug/app:/usr/src/app docker-hug:1.0
```

Note que a instância é nomeada "mpti2019" e que a porta 8000 do host é mapeada para a porta 8000 do container. Além disso o diretório "/Users/silviocs/hug_api/docker-hug/app" do host é mapeado para o diretório "/usr/src/app".

### Testando a API teste

Após iniciar a instância do container você pode testar os seus endpoints através do navegador ou utilizar o curl na linha de comando.

Utilizando o navegador:
```
localhost:8000/calc?valor=1.2
localhost:8000/teste/22/55
localhost:8000/endereco/59080060
localhost:8000/pic
```
Utilizando o curl:
```
curl -i "localhost:8000/calc?valor=1.2"
curl -i "localhost:8000/teste/22/55"
curl -i "localhost:8000/endereco/59080060"
curl -i "localhost:8000/pic"
```

### Verificando o endereço IP address da instância 'mpti2019'

```
docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mpti2019
```

### Verificando o mapeamento da port 8000

```
docker port mpti2019 8000
```

### Limpando tudo

Primeiro é necessário parar a execução da instância "mpti2019". Embora aqui utilizemos o nome que demos ao instanciar o container, poderia ser também utilizado o ID do container. 

```
docker container stop mpti2019
```

Removendo o container "mpti2019".

```
docker container rm mpti2019
```

Removendo a imagem "docker-hug:1.0".

```
docker image rm docker-hug:1.0
```
