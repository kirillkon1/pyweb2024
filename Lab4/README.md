# 4. Работа с портáми и томáми

---

### 1. Создание контейнера nginx, создание контейнера с WSGI-сервером на Python (с помощью docker run ...).
   ```bash
      docker run -d --name nginx-container -p 8081:80 nginx
   ```
    
**WSGI-сервер на Python**
   ```bash
       docker run -it --name wsgi-container -p 8082:80 python:3.9-slim bash
       pip install flask
   ```
Создание Flask проекта:
   ```bash
      nano app.py
   ```

   ```python
    from flask import Flask
    app = Flask(__name__)
    
    @app.route("/")
    def hello():
        return "Hello World!"
   ```
![img_2.png](images/img_2.png)
![img_1.png](images/img_1.png)
![img.png](images/img.png)

### 2. Создание образа nginx из Dockerfile (docker build), создание образа WSGI-сервером на Python


```dockerfile
#NGINX
FROM nginx:alpine
```
![img_3.png](images/img_3.png)

```dockerfile
#Python
FROM python:3.9-slim
WORKDIR /app
COPY ./app.py /app/
RUN pip install flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
```
![img_4.png](images/img_4.png)

#### Образы
![img_5.png](images/img_5.png)


### 3. Загрузка образа в докер хаб (Docker Hub). В отчете отобразить ссылку на образ с описанием.

### Образ NGINX:
```bash
docker tag custom-nginx kirillkon1/custom-nginx:latest
docker push kirillkon1/custom-nginx:latest
```
![img_6.png](images/img_6.png)
### Образ WSGI:
```bash
docker tag custom-wsgi kirillkon1/custom-wsgi:latest
docker push kirillkon1/custom-wsgi:latest
```
![img_7.png](images/img_7.png) 


### Ссылки на образы в Dockerhub
Образ NGINX: [https://hub.docker.com/r/kirillkon1/custom-nginx](https://hub.docker.com/r/kirillkon1/custom-nginx)

Образ WSGI Python: [https://hub.docker.com/r/kirillkon1/custom-wsgi](https://hub.docker.com/r/kirillkon1/custom-wsgi)

### 4. Использование docker-compose при работе с несколькими образами/контейнерами, томами. Создать docker-compose.yaml и реализовать в нем запуск одновременно nginx и WSGI-сервером на Python на разных портах 8081 и 8082.

#### docker-compose.yaml
```yaml
version: '3'
services:
  nginx:
    image: kirillkon1/custom-nginx:latest
    ports:
      - "8081:80"
    depends_on:
      - wsgi
  wsgi:
    image: kirillkon1/custom-wsgi:latest
    ports:
      - "8082:80"
```
```bash
docker-compose up
```

![img_9.png](images/img_9.png)
![img_8.png](images/img_8.png)