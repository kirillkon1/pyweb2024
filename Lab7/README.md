# Лабораторная работа №7. REST. FastAPI. Swagger

## Запуск проекта 

```bash
docker-compose up
```

![img.png](img/img.png)

## Демонстрация

### Swagger

![img_1.png](img/img_1.png)


### Получение списка всех терминов.

```
curl -X 'GET' \
  'http://localhost:8000/terms/?skip=0&limit=100' \
  -H 'accept: application/json'
```
![img_2.png](img/img_2.png)



### Получение информации о конкретном термине по ключевому слову.


``` 
curl -X 'GET' \
  'http://localhost:8000/terms/search/?keyword=test1' \
  -H 'accept: application/json'
```

![img_4.png](img/img_4.png)

### Получение термина по id

```
curl -X 'GET' \
  'http://localhost:8000/terms/1' \
  -H 'accept: application/json'
```

![img_5.png](img/img_5.png)

### Добавление нового термина с описанием.
```
curl -X 'POST' \
  'http://localhost:8000/terms/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "keyword": "test1",
  "description": "Test word 1"
}'
```
![img_3.png](img/img_3.png)

### Обновление существующего термина.

```
curl -X 'PUT' \
  'http://localhost:8000/terms/12' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "keyword": "Test Update",
  "description": "Test Update"
}'
```

![img_6.png](img/img_6.png)

### Удаление термина из глоссария.

``` 
curl -X 'DELETE' \
  'http://localhost:8000/terms/12' \
  -H 'accept: application/json'
```

![img_7.png](img/img_7.png)